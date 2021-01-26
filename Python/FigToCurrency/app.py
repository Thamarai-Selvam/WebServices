from flask import Flask, request, Response, jsonify
from flask_restful import Resource, Api, reqparse
from flask_ngrok import run_with_ngrok
import json

app = Flask(__name__)
run_with_ngrok(app)  # Start ngrok when app is run

#Sample UI
#-------------------------------------------------------------------------------
#
# Enter Numbers                  
#   -------------------        
#   |                 |       
#   -------------------    
#
#   -------------------------------     
#   | Currency in Words           |             OUTPUT
#   -------------------------------              __________________________
#                                                |                         |
#                                                |                         |
#                                                |_________________________| 
#-------------------------------------------------------------------------------

api = Api(app)

class FigureToCurrency(Resource):
  def get(self):
    print(request.args)

    number = int(request.args['value'])
    
    ones = ("", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine")
    tens = ("", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety")
    teens = ("ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen")
    levels = ("", "thousand", "million", "billion", "trillion", "quadrillion", "quintillion", "sextillion", "septillion", "octillion", "nonillion")

    word = ""
    orgNum = number
    num = reversed(str(number))
    number = ""
    for x in num:
        number += x
    del num
    if len(number) % 3 == 1: number += "0"
    x = 0
    for digit in number:
        if x % 3 == 0:
            word = levels[x // 3] + ", " + word
            n = int(digit)
        elif x % 3 == 1:
            if digit == "1":
                num = teens[n]
            else:
                num = tens[int(digit)]
                if n:
                    if num:
                        num += "-" + ones[n]
                    else:
                        num = ones[n]
            word = num + " " + word
        elif x % 3 == 2:
            if digit != "0":
                word = ones[int(digit)] + " hundred " + word
        x += 1
    return home(str(orgNum),word.strip(", "))


api.add_resource(FigureToCurrency, '/currency')

#common error handler
@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>Page not found.</p>", 404


@app.route('/', methods=['GET','POST'])
def home(gvalue="5001",value=""):
  return '''<!DOCTYPE html>
<html>
<head>
<title>Figures to Currency</title>
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
  width:150%;
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
<h1>Figures to Currency</h1>
<p>API Usage : Returns the words of given number value</p>
<p class="api_proc">API Call Format : <span>http://localhost:5000/currency?value=5001</span></p>
</div>
<div class="workarea">

<form action="/currency">
  <label for="message">Figures</label><br>
  <input type="text" id="value" name="value" value="'''+gvalue+'''"><br>
  <input type="submit" value="Submit">
</form>
<form class="response_form">
  <label for="response">Words</label><br>
  <input type="text" id="response" name="response" value="'''+value+'''"><br>
</form>

</div>
     
</body>
</html> 

'''

if __name__ == '__main__':
  app.run()
