
from flask import Flask, request, Response, jsonify
from flask_ngrok import run_with_ngrok
import json

app = Flask(__name__)
# run_with_ngrok(app)  # Start ngrok when app is run
import math
import struct
import sys

def prepare_message(message):

    paddingSize = (64 - 1 - 8 - len(message) % 64) % 64
    lengthInBits = (len(message) * 8) % 2 ** 64
    return message + b"\x80" + paddingSize * b"\x00" + struct.pack("<Q", lengthInBits)

def rotate_left(n, amount):
    return ((n << amount) & 0xffff_ffff) | (n >> (32 - amount))

def hash_chunk(state, chunk):
    (a, b, c, d) = state

    for i in range(64):
        if i < 16:
            bits = (b & c) | (~b & d)
            index = i
            shift = (7, 12, 17, 22)[i % 4]
        elif i < 32:
            bits = (d & b) | (c & ~d)
            index = (5 * i + 1) % 16
            shift = (5, 9, 14, 20)[i % 4]
        elif i < 48:
            bits = b ^ c ^ d
            index = (3 * i + 5) % 16
            shift = (4, 11, 16, 23)[i % 4]
        else:
            bits = c ^ (b | ~d)
            index = 7 * i % 16
            shift = (6, 10, 15, 21)[i % 4]

        const = math.floor(abs(math.sin(i + 1)) * 2 ** 32)
        bAdd = (const + a + bits + chunk[index]) & 0xffff_ffff
        bAdd = rotate_left(bAdd, shift)

        (a, b, c, d) = (d, (b + bAdd) & 0xffff_ffff, b, c)

    return (a, b, c, d)

def md5(message):

    # set initial state
    state = [0x67452301, 0xefcdab89, 0x98badcfe, 0x10325476]
    # prepare message and process it in chunks of 64 bytes (16 32-bit integers)
    ctr = 0
    for chunk in struct.iter_unpack("<16I", prepare_message(message)):
        print('chunk  ', chunk, 'ctr', ctr)
        ctr += 1
        print('prep-msg  ', prepare_message(message))
        print('iter-unpack  ', struct.iter_unpack("<16I", prepare_message(message)))
        # hash the chunk; add each 32-bit integer to the corresponding integer in the state
        hash_ = hash_chunk(state, chunk)
        state = [(s + h) & 0xffff_ffff for (s, h) in zip(state, hash_)]
    # the final state is the hash
    return b"".join(struct.pack("<I", number) for number in state)

@app.route('/checksum', methods=['GET'])
def getChecksum():

    message = request.args['message']
    return home(message,md5(message.encode("utf-8")).hex()), 200

#common error handler
@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>Page not found.</p>", 404

@app.route('/', methods=['GET','POST'])
def home(gvalue="AWord123",value=""):
  return '''<!DOCTYPE html>
<html>
<head>
<title>MD5 Checksum</title>
<style>
body {
  background-color: #4db8ff;
  text-align: center;
  color: white;
  font-family: Arial, Helvetica, sans-serif;
}
span {
	color : white;
    font-style: oblique;
}
.info {
	background-color : #0099ff;
    padding : 20px;
    margin: -10px -10px 0 -10px;
}
.api_proc {
	background-color: #6600cc;
    padding:7px;
    border-radius:20px;
}
.workarea {
text-align : left;
padding : 50px;
}

input[type=text] {
  width: 80%;
  padding: 12px 20px;
  margin: 8px 0;
  display: inline-block;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box;
  
}
input[type=submit] {
  width: 40%;
  background-color:   #00b359;
  color: white;
  padding: 10px 20px;
  margin: 8px 0;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size:17px;
}

input[type=submit]:hover {
  background-color: #00994d;
}
.response_form {
	padding-top:50px;
}
</style>
</head>
<body>
<div class="info">
<h1>MD5 Checksum</h1>
<p>API Usage : Returns the MD5 checksum of given value</p>
<p class="api_proc">API Call Format : <span>http://localhost:5000/checksum?value=AWord123</span></p>
</div>
<div class="workarea">

<form action="/checksum">
  <label for="message">Message</label><br>
  <input type="text" id="message" name="message" value="'''+gvalue+'''"><br>
  <input type="submit" value="Submit">
</form>
<form class="response_form">
  <label for="response">Checksum</label><br>
  <input type="text" id="response" name="response" value="'''+value+'''"><br>
</form>

</div>
     
</body>
</html> 

'''

if __name__ == "__main__":
  app.run()