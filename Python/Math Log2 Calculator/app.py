from flask import Flask, request, Response, jsonify
from flask_restful import Resource, Api, reqparse
from flask_ngrok import run_with_ngrok
import json
import math

app = Flask(__name__)

def rgcf(x, y) :

    if (x == 0):
        return y
    return rgcf(y % x, x)


def gcf(data) :

    tempRes = data[0]
   
    for element in data:
        tempRes = rgcf(element, tempRes)
    if (tempRes == 1):
        return 1
    return tempRes


def rlcm(x, y) :
    return 0 if (not x or not y) else abs((x * y) / rgcf(x, y))


def lcm(data) :
    tempRes = data[0]
    for element in data:
        tempRes = rlcm(element, tempRes)

    if (tempRes == 1):
        return 1
    return tempRes



@app.route('/log2', methods=['GET'])
def getHandler():

    print(request.args)
    opChoice = int(request.args['opChoice'])
    
    if(opChoice == 0 and not request.args.get('data')):
        return 'Enter Numbers set to find GCD and LCM', 500
    elif(opChoice == 2 and not request.args.get('num3') and not request.args.get('pow')):
        return 'Enter Number and Power to find Nth Root', 500
    elif(opChoice == 2 and not request.args.get('num')):
        return 'Enter Number find Square and Cube Root', 500

    vOpName = data = pow = num = num3 = 0
    if (opChoice == 0):
        data = list(map(int,request.args['data'].split(',')))

        vOpName = "GCF and LCM of "
        vresult = str(gcf(data)) + " and " + str(lcm(data))
    elif (opChoice == 1):
        data =  int(request.args['num'])

        vresult = str(data**(1/2)) + ' and ' + str(data**(1/3))
        vOpName = "Square Root and Cube Root of "

    elif (opChoice == 2):
        data = int(request.args['num3'])
        pow = int(request.args['pow'])
        vresult = data**(1/float(pow))

        vOpName = '<sup>'+str(pow)+'</sup>√'+str(data)
        pow = data = ''

    
    if (vresult):
        return home(str(data),str(vresult),str(vOpName), str(pow), str(data), str(data))
    else:
        return 'Invalid Data !', 500
    
@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>Page not found.</p>", 404


@app.route('/', methods=['GET','POST'])
def home(data="1",result="",opName='', pow='', num='', num3=''):
  return '''<!DOCTYPE html>
<html>

<head>
    <title>Math Log2 Calculator</title>
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
        <h1>Math Log2 Calculator</h1>
        <p>API Usage : Returns the result of selected log2 operations</p>

    </div>
    <div class="workarea">
        <form action="/log2">
            <center> <select name="opChoice" id="opChoice" onchange="changeset()">
                <option id="gcflcm" value="0" selected="true">GCF and LCM</option>
                <option id="sqcrt" value="1">Square and Cube Root</option>
                <option id="nrt" value="2">N<sup>th</sup> Root</option>
            </select></center>
            </br>

            <div id="opset1" style="display: block;">
                <label for="data">Enter the data (Ex. 2,4,6,8):</label>
                <input type="text" id="data" name="data" value="'''+data+'''"></br>
            </div>
            <div id="opset2" style="display: none;">
                <label for="data">Enter Number:</label>
                <input type="text" id="num" name="num" value="'''+num+'''"></br>
            </div>
            <div id="opset3" style="display: none;">
                <label for="data">Enter Number : </label>
                <input type="text" id="num3" name="num3" value="'''+num3+'''"></br>
                <label for="data">Enter Root : </label>
                <input type="text" id="pow" name="pow" value="'''+pow+'''"></br>
            </div>
            <input type="submit" value="Submit">
        </form>

        <form class="response_form">
            <label for="result">'''+opName+' ' +data+''' : </label>
            <input type="text" id="result" name="result" value="'''+result+'''"</br>

        </form>
    </div>

    <script>
        function changeset() {
            const opChoice = document.getElementById('opChoice').value;
            if (opChoice == '0') {
                document.getElementById('opset1').style.display = "block"
                document.getElementById('opset2').style.display = "none"
                document.getElementById('opset3').style.display = "none"
                document.getElementById('result').value = ""

            } else if (opChoice == '1') {
                document.getElementById('opset1').style.display = "none"
                document.getElementById('opset2').style.display = "block"
                document.getElementById('opset3').style.display = "none"
                document.getElementById('result').value = ""

            } else {
                document.getElementById('opset1').style.display = "none"
                document.getElementById('opset2').style.display = "none"
                document.getElementById('opset3').style.display = "block"
                document.getElementById('result').value = ""

            }


        }
    </script>
</body>

</html>
'''

if __name__ == '__main__':
  app.run(debug=True)