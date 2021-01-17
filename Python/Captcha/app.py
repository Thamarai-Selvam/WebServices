import random
import numpy as np
from PIL import Image, ImageFont,ImageDraw
import glob
import string
import cv2
import os,io
from flask import Flask, request, Response, make_response

app = Flask(__name__)

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
	font = ImageFont.truetype(random.choice(fonts), size)
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
	return response
@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>Page not found.</p>", 404
if __name__ == "__main__":
   app.run()