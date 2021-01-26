import random
import numpy as np
from PIL import Image, ImageFont,ImageDraw
import glob
import string
import cv2
import os,io
from io import BytesIO
import base64
from flask_ngrok import run_with_ngrok
from flask import Flask, request, Response, make_response

app = Flask(__name__)
run_with_ngrok(app)  # Start ngrok when app is run


@app.route('/getcaptcha', methods=['GET'])
def getCaptcha():
	
	text = request.args['value']
	# Setting up the canvas
	size = random.randint(10,50)
	length = len(text)
	img = np.zeros(((size*2)+5, length*size, 3), np.uint8)
	img_pil = Image.fromarray(img+255)
	
	# Drawing text and lines
	fontsPath = r"C:\Windows\Fonts"
	fonts = glob.glob(fontsPath+"\\ari*.ttf")
	font = ImageFont.truetype("Roboto-Regular.ttf", size)
	draw = ImageDraw.Draw(img_pil)
	draw.text((5, 10), text, font=font, 
	          fill=(random.randint(0,255), random.randint(0,255), random.randint(0,255)))
	draw.line([(random.choice(range(length*size)), random.choice(range((size*2)+5)))
           ,(random.choice(range(length*size)), random.choice(range((size*2)+5)))]
          , width=1, fill=(random.randint(0,255), random.randint(0,255), random.randint(0,255)))

	# Adding noise and blur
	img = np.array(img_pil)
	thresh = random.randint(1,5)/100
	for i in range(img.shape[0]):
	    for j in range(img.shape[1]):
        	rdn = random.random()
	        if rdn < thresh:
	            img[i][j] = random.randint(0,123)
	        elif rdn > 1-thresh:
        	    img[i][j] = random.randint(123,255)
	img = cv2.blur(img,(int(size/random.randint(5,10)),int(size/random.randint(5,10))))

	#Displaying image
	#cv2.imshow(f"{text}", img)
	#cv2.waitKey()
	#cv2.destroyAllWindows()
	#cv2.imwrite(f"{os.getcwd()}\{text}.png", img) #if you want to save the image
	retval, buffer = cv2.imencode('.png', img)
	response = Response(buffer.tobytes(), mimetype="image/png")
	return home(text,pil2datauri(buffer.tobytes()))
 
def pil2datauri(img):
    #converts PIL image to datauri
    data = BytesIO()
    # img.save(data, "JPEG")
    data64 = base64.b64encode(img)
    return u'data:img/jpeg;base64,'+data64.decode('utf-8')

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>Page not found.</p>", 404


@app.route('/', methods=['GET','POST'])
def home(value="AWord123",img=""):
  print(str(value))
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
<p class="api_proc">API Call Format : <span>http://localhost:5000/getcaptcha?value=AWord123</span></p>
</div>
<div class="workarea">

<form action="/getcaptcha">
  <label for="message">CAPTCHA Content</label><br>
  <input type="text" id="value" name="value" value="'''+value+'''"><br>
  <input type="submit" value="Submit">
</form>
<form class="response_form">
  <label for="response">CAPTCHA</label><br>
  <img src="'''+img+'''"></img></form>
</div>

</body>
</html>
'''


if __name__ == "__main__":
   app.run()