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


@app.route('/log1', methods=['GET'])
def getHandler():

    print(request.args)
    opChoice = int(request.args['opChoice'])
    
    if(opChoice == 0 and not request.args.get('num3') and not request.args.get('base')):
        return 'Enter Number and Base to find Log', 500
    elif(opChoice == 1 and not request.args.get('num')):
        return 'Enter Number to find Natural Log', 500
    elif(opChoice == 2 and not request.args.get('data') and not request.args.get('pow')):
        return 'Enter Number and Power to find Antilog', 500

    vOpName = data = pow = num = num3 = 0
    
    if (opChoice == 0):
        data = int(request.args['num3'])
        base = int(request.args['base'])

        vOpName = "Log "
        vresult = log(data, base)
    elif (opChoice == 1):
        data = int(request.args['num'])

        vresult = nLog(data)
        vOpName = "Natural Log "

    elif (opChoice == 2):
        data = int(request.args['data'])
        pow = int(request.args['pow'])
        vresult = antiLog(data, pow)
        vOpName = "AntiLog "
    
    if (vresult):
        return home(str(data),str(vresult),str(vOpName), str(pow), str(data), str(data))
    else:
        return 'Invalid Data !', 500
    
@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>Page not found.</p>", 404


@app.route('/', methods=['GET','POST'])
def home(data="1",result="",opName='', pow='', num='', num3='', base=''):
  return '''<!DOCTYPE html>
<html>

<head>
    <title>Math Log1 Calculator</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/js/bootstrap.bundle.min.js" integrity="sha384-ygbV9kiqUc6oa4msXn9868pTtWMgiQaeYH7/t7LECLbyPA2x65Kgf80OJFdroafW" crossorigin="anonymous"></script>
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
        span {
	        color : white;
            font-style: oblique;
        }
        .info {
            background-color : #0099ff;
            padding : 20px;
            margin: -10px -50px 0 -50px;
        }
        .api_proc {
            background-color: #6600cc;
            padding:7px;
            border-radius:20px;
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

<body class="container">
    <div class="row info">
        <h1>Math Log1 Calculator</h1>
        <p>API Usage : Returns the result of selected log1 operations</p>

    </div>

    <div class="workarea">
        <form action="/log1">
            <center> <select name="opChoice" id="opChoice" onchange="changeset()">
                <option id="log" value="0" selected='true'>Logarithm(log)</option>
                <option id="nlog" value="1">Natural Logarithm (ln)</option>
                <option id="antilog" value="2"> Anti-logarithm </option>
            </select></center>
            </br>
            <div id="opset1" style="display: block;">
                <label for="data">Enter Number : </label>
                <input type="text" id="num3" name="num3" value="'''+num3+'''"></br>
                <label for="data">Enter Base : </label>
                <input type="text" id="base" name="base" value="'''+base+'''"></br>
            </div>

            <div id="opset2" style="display: none;">
                <label for="data">Enter Number:</label>
                <input type="text" id="num" name="num" value="'''+num+'''"></br>
            </div>
            <div id="opset3" style="display: none;">
                <label for="data">Enter Number:</label>
                <input type="text" id="data" name="data" value="'''+data+'''"></br>
                <label for="data">Enter Power:</label>
                <input type="text" id="pow" name="pow" value="'''+pow+'''"></br>
            </div>
            <input type="submit" value="Submit">
        </form>

        <form class="response_form">
            <label for="result">'''+opName+'''of '''+data+''' : </label>
            <input type="text" id="result" name="result" value="'''+result+'''"></br>

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