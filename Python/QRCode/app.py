from flask import Flask, request, Response
from flask_ngrok import run_with_ngrok
import math, random 
import base64
import pyqrcode 
import png 
import io
from pyqrcode import QRCode 
app = Flask(__name__)
# run_with_ngrok(app)  # Start ngrok when app is run


#common error handler
@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>Page not found.</p>", 404


@app.route('/qrcode', methods=['GET'])
def qrcode():
    message = request.args['value']
    url = pyqrcode.create(message)
    print(url)
    s = io.BytesIO()
    url.png(s,scale=6)
    encoded = u'data:img/jpeg;base64,'+str(base64.b64encode(s.getvalue()).decode("ascii"))
    return home(message,encoded) 


@app.route('/', methods=['GET','POST'])
def home(value="AWord123",img=""):
  print(str(value))
  return '''<!DOCTYPE html>
<html>
<head>
<title>QRCode</title>
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
<h1>QRCode</h1>
<p>Returns the Image QRCode out of the given message </p>
<p class="api_proc">API Call Format : <span>http://localhost:5000/qrcode?value=AWord123</span></p>
</div>
<div class="workarea">

<form action="/qrcode">
  <label for="message">QRCode Content</label><br>
  <input type="text" id="value" name="value" value="'''+value+'''"><br>
  <input type="submit" value="Submit">
</form>
<form class="response_form">
  <label for="response">Barcode</label><br>
  <img src="'''+img+'''"></img></form>
</div>

</body>
</html>
'''


if __name__ == "__main__":
   app.run(debug=True)