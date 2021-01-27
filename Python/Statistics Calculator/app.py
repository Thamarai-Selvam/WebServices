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
    return math.sqrt(data)

def lrReg(data):
    return data


@app.route('/statcalc', methods=['GET'])
def rootStat():
    
    # try:
    ipArr = list(map(int,request.args['data'].split(',')))
    print(*ipArr)
    
    variance = Variance(ipArr)
    stDev = stdDev(variance)
    lReg = lrReg(ipArr)

    return home(request.args['data'], str(stDev), str(variance), str(lReg)) 
    # except:
    #     return "Invalid Format, Enter Comma Seperated Values, (Ex. 1,2,3,4)", 500




   




@app.route('/', methods=['GET','POST'])
def home(data="1,2,3,4,5,6", stDev="" ,variance="", lReg=""):


  return '''<!DOCTYPE html>
<html>
<head>
<title>Statistics calculator</title>
<style>

</style>
</head>
<body>
<div class="info">
<h1> Statistics calculator </h1>
</div>
<div class="workarea">
  <form action="/statcalc">
    <label for="data">Enter the data:</label>
    <input type="text" id="data" name="data" value="'''+data+'''">

    <input type="submit" value="Submit">
  </form>

  <form class="response_form">
   <label for="variance">Variance : </label>
    <input type="text" id="variance" name="variance" value="'''+variance+'''">
    <label for="stdev">Standard Deviation : </label>
    <input type="text" id="stdev" name="stdev" value="'''+stDev+'''">
    <label for="lreg">Linear Regression : </label>
    <input type="text" id="lreg" name="lreg" value="'''+lReg+'''">
  </form>
</div>
</body>
</html>

  '''

if __name__ == '__main__':
  app.run(debug=True)