from flask import Flask, request, Response, jsonify
from flask_restful import Resource, Api, reqparse
from flask_ngrok import run_with_ngrok
import json
import math

app = Flask(__name__)
PI = 3.141592653589793
def getsin(number):

    number %= 2 * PI
    if (number < 0) :
        number = 2 * PI - number
    

    sign = 1
    if (number > PI) :
        number -= PI
        sign = -1
    

    PRECISION = 50
    temp = 0
    for i in range(PRECISION + 1) :
        temp += math.pow(-1, i) * (math.pow(number, 2 * i + 1) / fact(2 * i + 1))
    
    result = sign * temp
    return result


def getCos(number):
    number = (PI / 2) - number
    return getsin(number)



def fact(num):
    if (num == 0 or num == 1):
        return 1
    else:
        return num * fact(num - 1)



def getTrigResult(x, op, degType):

    if (op <= 5 and degType == 0):
         x *= PI / 180
    if (op == 0): y = getsin(x); #y = Math.sin(x);
    elif (op == 1): y = getCos(x)
    elif (op == 2): y = getsin(x) / getCos(x)
    elif (op == 3): y = 1 / getsin(x)
    elif (op == 4): y = 1 / getCos(x)
    elif (op == 5): y = getCos(x) / getsin(x)
    elif (op == 6): y = math.asin(x)
    elif (op == 7): y = math.acos(x)
    elif (op == 8): y = math.atan(x)
    elif (op == 9): y = 1/math.asin(x)
    elif (op == 10): y = 1/math.acos(x)
    else: y = 1/math.atan(x)
    if (op >= 6 and degType == 0): y *= 180 / PI
    y = round(y, 8)
    return y

@app.route('/log3', methods=['GET'])
def getTrigHandler():

    print(request.args)

    if(not request.args.get('opChoice') or not request.args.get('data')):
        return 'Select a function or Enter data', 500
    data = float(request.args['data'])
    opChoice = int(request.args['opChoice'])
    degType = int(request.args['degType'])
    if(opChoice >= 6 and data > 1):
          return 'Arc(sin,cos,tan,cosec,sec,cot) can\'t be greater than 1 !', 500
   
    result = getTrigResult(data, opChoice, degType)
    if (result):
        return home(str(data),str(result))
    else:
        return 'Invalid Data !', 500
    
@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>Page not found.</p>", 404


@app.route('/', methods=['GET','POST'])
def home(data="1",result=""):
  return '''<!DOCTYPE html>
<html>

<head>
    <title>Math Log3 Calculator</title>
    <style>
        body {
            background-color: #4db8ff;
            text-align: center;
            color: white;
            font-family: Arial, Helvetica, sans-serif;
        }
        
        .workarea {
            padding: 50px;
        }
        
        input[type=text] {
            width: 60%;
            padding: 12px 20px;
            margin: 8px 0;
            display: inline-block;
            border: 1px solid #ccc;
            border-radius: 4px;
            box-sizing: border-box;
        }
        
        input[type=submit] {
            width: 10%;
            background-color: #00b359;
            color: white;
            padding: 10px 20px;
            margin: 8px 0;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 17px;
        }
        
        input[type=submit]:hover {
            background-color: #00994d;
        }
        
        .response_form {
            padding-top: 50px;
        }
    </style>
</head>

<body>
    <div class="info">
        <h1>Math Log3 Calculator</h1>
        <p>API Usage : Returns the result of selected log3 trignometry operations</p>

    </div>
    <div class="workarea">
        <form action="/log3">
            <select name="opChoice" id="opChoice">
                <option id="blankOption" selected="true" disabled="disabled" >-- Select an Option --</option>
                <option id="sin" value="0">sin</option>
                <option id="cos" value="1">cos</option>
                <option id="tan" value="2">tan</option> 
                <option id="cosec" value="3">cosec</option>
                <option id="sec" value="4">sec</option>
                <option id="cot" value="5">cot</option>
                <option id="arcsin" value="6">arcsin</option>
                <option id="arccos" value="7">arccos</option>
                <option id="arctan" value="8">arctan</option>
                <option id="arccosec" value="9">arccosec</option>
                <option id="arcsec" value="10">arcsec</option>
                <option id="arccot" value="11">arccot</option>
            </select>

            <div id="opset1" style="display: inline-block;">
                <label for="data"></label>
                <input type="text" id="data" name="data" value="'''+data+'''"></br>
            </div>
            <select name="degType" id="degType">
                <option id="deg" value="0" selected="true">deg</option>
                <option id="rad" value="1">rad</option> 
            </select>
            </br>
            <input type="submit" value="Submit">
        </form>
        <form class="response_form">
            <label for="result">Result: </label>
            <input type="text" id="result" name="result" value="'''+result+'''"></br>
        </form>
    </div>

</body>

</html>
'''

if __name__ == '__main__':
  app.run(debug=True)