!pip install flask_restful
!pip install flask_ngrok

from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_ngrok import run_with_ngrok
import math, random 

app = Flask(__name__)
run_with_ngrok(app)  # Start ngrok when app is run

#Sample UI
#-------------------------------------------------------------------------------
#
# Enter length               
#   -------------------         
#   |                 |        
#   -------------------       
#
#    OUTPUT____________________
#    |                         |
#    |                         |
#    |_________________________| 
#-------------------------------------------------------------------------------

#common error handler
@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>Page not found.</p>", 404

#---------------Tranpose--------------------
@app.route('/otp', methods=['GET'])
def otpGen():
  
  length = int(request.args['length'])
  typeOtp = int(request.args['typeotp'])
  if (typeOtp == 0):
    typeContents = "1234567890"
  elif (typeOtp == 1):
    typeContents = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
  else:
    typeContents = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
  
  genOTP = "" 

  for i in range(length) : 
      genOTP += typeContents[math.floor(random.random() * len(typeContents))] 

  return home(str(length),str(typeOtp),genOTP)


@app.route('/', methods=['GET','POST'])
def home(len='4', typeotp='0',value=""):
  return '''<!DOCTYPE html>
<html>
<head>
<title>CAPTCHA</title>
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
<h1>CAPTCHA</h1>
<p>Returns the Image CAPTCHA out of the given message </p>
<p class="api_proc">API Call Format : <span>http://localhost:5000/otp?length=4&typeotp=</span></p>
</div>
<div class="workarea">

<form action="/otp">
  <label for="message">OTP Length</label><br>
  <input type="text" id="length" name="length" value="'''+len+'''"><br>
  <label for="message">Type( 0 - Numeric, 1 - Alphabets, 2 - Alphanumeric)</label><br>
  <input type="text" id="typeotp" name="typeotp" value="'''+typeotp+'''"><br>
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

if __name__ == '__main__':
  app.run()
