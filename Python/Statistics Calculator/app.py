import math

from flask import Flask, request

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>Page not found.</p>", 404


#-----------------------Logic #3----------------------------------------------------------------------


 

def Variance(data):
    n = len(data)
    mean = sum(data) / n
    deviations = [( x- mean) **2 for x in data]
    variance = sum(deviations) / n
    return variance

def stdDev(data):
    return math.sqrt(Variance(data))

def lrReg(X, Y):
    sumX = sum(X)
    sumY = sum(Y)
    sumXX = 0
    sumXY = 0
    for i in range(len(X)):
        sumXX += X[i] * X[i]
        sumXY += X[i] * Y[i]

    print(sumX, sumY, sumXX, sumXY)

    n = len(X)

    a = ((sumY * sumXX) - (sumX * sumXY)) / ((n * sumXX) - (sumX * sumX))
    b = ((n * sumXY) - (sumX * sumY)) / ((n * sumXX) - (sumX * sumX))

    # REGRESSION EQUATION = > Y = a + bx
    return f"{a} + {b}(x)"


@app.route('/statcalc', methods=['GET'])
def rootStat():
    
    # try:
    
    
    opChoice = int(request.args['opChoice'])
    print(request.args)
    data = data1 = data2 = result = ''
    if (opChoice == 0) :
        data = list(map(int,request.args['data'].split(',')))
        result = stdDev(data)
    elif (opChoice == 1) :
        data = list(map(int,request.args['data'].split(',')))
        result = Variance(data)
    else :
        data1 = list(map(int,request.args['data1'].split(',')))
        data2 = list(map(int,request.args['data2'].split(',')))
        result = lrReg(data1, data2)
    
    

    return home(request.args['data'], str(data1), str(data2),str(result)) 


@app.route('/', methods=['GET','POST'])
def home(data="1,2,3,4,5,6",  data1='', data2='', result=''):


  return '''<!DOCTYPE html>
<html>
<head>
<title>Statistics calculator</title>
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
<h1> Statistics calculator </h1>
</div>
 <div class="workarea">
        <form action="/statcalc">
            <center> <select name="opChoice" id="opChoice" onchange="changeset()">
                <option id="stdev" value="0" selected='true'>Standard Deviation</option>
                <option id="variance" value="1">Variance</option>
                <option id="lreg" value="2">Linear Regression</option>
            </select></center>
            </br>

            <div id="opset1" style="display: block;">
                <label for="data">Enter the data (Ex. 2,4,6,8):</label>
                <input type="text" id="data" name="data" value="'''+data+'''"></br>
            </div>
            <div id="opset2" style="display: none;">
                <label for="data">Enter X set  (Ex. 2,4,6,8): </label>
                <input type="text" id="data1" name="data1" value="'''+data1+'''"></br>
                <label for="data1">Enter Y set (Ex. 2,4,6,8): </label>
                <input type="text" id="data2" name="data2" value="'''+data2+'''"></br>
            </div>
            <input type="submit" value="Submit">
        </form>

        <form class="response_form">
            <label for="result">Result</label>
            <input type="text" id="result" name="result" value="'''+result+'''"></br>

        </form>
    </div>

    <script>
        function changeset() {
            const opChoice = document.getElementById('opChoice').value;
            if (opChoice == '0') {
                document.getElementById('opset1').style.display = "block"
                document.getElementById('opset2').style.display = "none"
                document.getElementById('result').value = ""

            } else if (opChoice == '2') {
                document.getElementById('opset1').style.display = "none"
                document.getElementById('opset2').style.display = "block"
                document.getElementById('result').value = ""

            }


        }
    </script>
</body>
</html>

  '''

if __name__ == '__main__':
  app.run(debug=True)