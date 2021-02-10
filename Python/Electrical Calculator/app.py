from flask import Flask, request, Response, jsonify
from flask_restful import Resource, Api, reqparse
from flask_ngrok import run_with_ngrok
import json
import math

app = Flask(__name__)


def nLog(x) :
    n = 99999999
    return n * ((x ** (1 / n)) - 1)


def log(x, base) :
    try:
        result = nLog(x) / nLog(base)
    except:
        result = 'Infinity'
    return result


def antiLog(a, b) :

    c = 1
    for i in range(1,b+1):
        c = c * a
    return c


@app.route('/ecalc', methods=['GET'])
def getHandler():

    print(request.args)
    vChoice = int(request.args['vChoice'])
    aChoice = int(request.args['aChoice'])
    a = int(request.args['num'])
    v = int(request.args['num1'])



    if (aChoice == 0):
        a /= 1000
    elif (aChoice == 1):
        a = a
    else:
        a *= 1000
    if (vChoice == 0):
        v /= 1000
    elif (vChoice == 1):
        v = v
    else:
        v *= 1000

    iw = a * v
    ikw = a * v / 1000
    imw = a * v * 1000
   
    if (iw):
        #  return {'Amps' :request.args['num'],
        #     'Volts':request.args['num1'],
        #     'Watts' : iw,
        #     'MilliWatts': imw,
        #     'kiloWatts':ikw }
        return home(str(request.args['num']),str(request.args['num1']),str(imw), str(iw), str(ikw))
    else:
        return 'Invalid Data !', 500
    
@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>Page not found.</p>", 404


@app.route('/', methods=['GET','POST'])
def home(num='10', num1='12',mw='',w='',kw=''):
  return '''<!DOCTYPE html>
<html>

<head>
    <title>Electrical Calculator</title>
    <style>
        body {
            background-color: #4db8ff;
            text-align: center;
            color: white;
            font-family: Arial, Helvetica, sans-serif;
        }
        
        .workarea {
            text-align: left;
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
            width: 40%;
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
        <h1>Electrical Calculator</h1>
        <p>API Usage : Returns the result of selected electrical unit operations</p>

    </div>

    <div class="workarea">
        <form action="/ecalc">

            </br>
            <div id="opset1" style="display: block;">
                <label for="data">Enter Current in amps : </label></br>
                <input type="text" id="num" name="num" value="'''+num+'''">
                <select name="aChoice" id="opChoice">
                    <option id="ma" value="0">mA</option>
                    <option id="a" selected="true" value="1">A</option>
                    <option id="ka" value="2">kA</option>
                    </select></br>
                <label for="data">Enter Current in volts   : </label></br>
                <input type="text" id="num1" name="num1" value="'''+num1+'''">
                <select name="vChoice" id="opChoice">
                    <option id="mv"  value="0">mv</option>
                    <option id="v" selected="true"value="1">V</option>
                    <option id="kv" value="2">kV</option>

                </select></br>
            </div>


            <input type="submit" value="Submit">
        </form>

        <form class="response_form">
            <label for="kw">Power result in kilowatts: </label></br>
            <input type="text" id="kw" name="kw" value="'''+kw+'''"></br>
            <label for="w">Power result in watts: </label></br>
            <input type="text" id="w" name="w" value="'''+w+'''"></br>
            <label for="mw">Power result in milliwatts: </label></br>
            <input type="text" id="mw" name="mw" value="'''+mw+'''"></br>

        </form>
    </div>

</body>

</html>
'''

if __name__ == '__main__':
  app.run(debug=True, port=3000)