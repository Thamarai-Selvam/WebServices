
from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_ngrok import run_with_ngrok



app = Flask(__name__)
run_with_ngrok(app)  # Start ngrok when app is run

#sample https:://127.0.0.1/datediff?fromYear=2020?fromMonth=06?fromDate=15?fromHour=0?fromMinute=1?fromSeconds=1?toYear=2020?toMonth=06?toDate=30?toHour=0?toMinute=10?toSeconds=1

#Sample UI
#---------------------------------------------------------------
#
# Enter From date             Enter To Date
#   -------------------         --------------------
#   |                 |         |                  |
#   -------------------         --------------------
#
#   ------------
#   | GET DIFF |                OUTPUT____________________
#   ------------                |                         |
#                               |                         |
#                               |_________________________| 
#-----------------------------------------------------------------

#----------------------------Logic #1---------------------------------------------------------
#----------------------------Get,Validate,Set Values--------------------------------------
api = Api(app)

#common error handler
@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>Page not found.</p>", 404


#-----------------------Logic #3----------------------------------------------------------------------

Months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

class Date:
    def __init__(self, year, month, date, hour, minute, seconds):
        self.date = date
        self.month = month
        self.year = year
        self.hour = hour
        self.minute = minute
        self.seconds = seconds



def getDifference(fromDate, toDate):

  if (toDate.seconds >= fromDate.seconds):
    rSeconds = toDate.seconds - fromDate.seconds
  else:
    rSeconds = (toDate.seconds + 60) - fromDate.seconds
    toDate.minute -= 1
  
  if (toDate.minute >= fromDate.minute):
    rMinutes = toDate.minute - fromDate.minute
  else:
    rMinutes = (toDate.minute + 60) - fromDate.minute
    toDate.hour -= 1

  if (toDate.hour >= fromDate.hour):
    rHours = toDate.hour - fromDate.hour
  else :
    rHours = (toDate.hour + 24) - fromDate.hour
    toDate.date -= 1
    
  if (toDate.date >= fromDate.date):
    rDays = toDate.date - fromDate.date - 1
  else : 
    rDays = (toDate.date + Months[toDate.month]) - fromDate.date - 2
    toDate.month -= 1

  if (toDate.month >= fromDate.month):
    rMonths = toDate.month - fromDate.month
  else:
    rMonths = (toDate.month + 12) - fromDate.month
    toDate.year -= 1
  
  if (toDate.year >= fromDate.year):
    rYears = toDate.year - fromDate.year
  else :
    rYears = 0
    

  return Date(rYears,rMonths, rDays, rHours, rMinutes, rSeconds)


class DateDifference(Resource):
  def get(self):
    print(request.args)
    if 1000 <= int(request.args['fromYear']) <= 9999 and 1000 <= int(request.args['toYear']) <= 9999:
      if 1 <= int(request.args['fromMonth']) <= 12 and 1 <= int(request.args['toMonth']) <= 12:
        if 1 <= int(request.args['fromDate']) <= 31 and 1 <= int(request.args['toDate']) <= 31:
          if 0 <= int(request.args['fromHour']) <= 24 and 0 <= int(request.args['toHour']) <= 24:
            if 0 <= int(request.args['fromMinute']) <= 31 and 0 <= int(request.args['toMinute']) <= 31:
              if 0 <= int(request.args['fromSeconds']) <= 31 and 0 <= int(request.args['toSeconds']) <= 31:
                fromDate  =  Date(int(request.args['fromYear']),int(request.args['fromMonth']), int(request.args['fromDate']), int(request.args['fromHour']), int(request.args['fromMinute']), int(request.args['fromSeconds']))
                toDate    =  Date(int(request.args['toYear']),int(request.args['toMonth']), int(request.args['toDate']), int(request.args['toHour']), int(request.args['toMinute']), int(request.args['toSeconds']))
              else : return 'Invalid Seconds !', 200
            else : return 'Invalid Minutes !', 200
          else : return 'Invalid Hour !', 200
        else : return 'Invalid Date !', 200
      else : return 'Invalid Month !', 200
    else : return 'Invalid Year !', 200

    
    print('from : ', fromDate,'\nto : ',toDate)
    rDate = getDifference(fromDate, toDate)
    print(f"{rDate.year} Year(s) {rDate.month} Month(s) {rDate.date} Day(s) {rDate.hour} Hour(s) {rDate.minute} Minute(s) {rDate.seconds} Second(s)")
    return home('',str(fromDate.date), str(fromDate.month), str(fromDate.year),str(fromDate.hour),
                str(fromDate.minute),str(fromDate.seconds),str(toDate.date), str(toDate.month),str(toDate.year), 
                str(toDate.hour),str(toDate.minute),str(toDate.seconds),
                f"{rDate.year} Year(s) {rDate.month} Month(s) {rDate.date} Day(s) {rDate.hour} Hour(s) {rDate.minute} Minute(s) {rDate.seconds} Second(s)", True)

api.add_resource(DateDifference, '/datediff')


@app.route('/', methods=['GET','POST'])
def home(responseLabel='',fromDate='10',fromMonth='01',fromYear='2020',fromHour='10',fromMinute='13',fromSeconds='31',toDate='12',toMonth='05',toYear='2021',toHour='02',toMinute='25',toSeconds='26',value="", isDone=False):
  if (isDone):
    responseLabel = str('Difference b/w '+fromDate+'/'+fromMonth+'/'+fromYear+' '+fromHour+' : '+fromMinute+' : '+fromSeconds+' And '+toDate+'/'+toMonth+'/'+toYear+' '+toHour+' : '+toMinute+' : '+toSeconds+' is '+value)
    print(responseLabel)
  return '''<!DOCTYPE html>
<html>
<head>
<title>Date Difference</title>
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
  width:15%;
  padding: 12px 10px;
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
<h1>Date Difference</h1>
<p>API Usage : Returns the difference b/w two given dates</p>
<p class="api_proc">API Call Format : <span>http://localhost:5000/datediff?fromYear=2020&fromMonth=07&fromDate=15&fromHour=0&fromMinute=1&fromSeconds=1&toYear=2020&toMonth=09&toDate=30&toHour=0&toMinute=10&toSeconds=1</span></p>
</div>
<div class="workarea">


  <form action="/datediff">
    <label for="fromDate">From Date Time</label><br>
    <div id="fromBlock" name="fromBlock">
    <label for="fromYear">Year</label>
    <input type="text" id="fromYear" name="fromYear" value="'''+fromYear+'''">
    <label for="fromMonth">Month</label>
    <input type="text" id="fromMonth" name="fromMonth" value="'''+fromMonth+'''">
    <label for="fromDate">Date</label> 
    <input type="text" id="fromDate" name="fromDate" value="'''+fromDate+'''">
    <br>
    <label for="fromHour">Hour</label>
    <input type="text" id="fromHour" name="fromHour" value="'''+fromHour+'''">
    <label for="fromMinute">Minute</label>
    <input type="text" id="fromMinute" name="fromMinute" value="'''+fromMinute+'''">
    <label for="fromSeconds">Seconds</label>
    <input type="text" id="fromSeconds" name="fromSeconds" value="'''+fromSeconds+'''">
    </div><br>
    <label for="toBlock">To Date Time</label><br>
    <div id="toBlock" name="toBlock">
    
    <label for="toYear">Year</label>
    <input type="text" id="toYear" name="toYear" value="'''+toYear+'''">
    <label for="toMonth">Month</label>
    <input type="text" id="toMonth" name="toMonth" value="'''+toMonth+'''">
    <label for="toDate">Date</label>
    <input type="text" id="toDate" name="toDate" value="'''+toDate+'''">
    <br>
    <label for="toHour">Hour</label>
    <input type="text" id="toHour" name="toHour" value="'''+toHour+'''">
    <label for="toMinute">Minute</label>
    <input type="text" id="toMinute" name="toMinute" value="'''+toMinute+'''">
    <label for="toSeconds">Seconds</label>
    <input type="text" id="toSeconds" name="toSeconds" value="'''+toSeconds+'''">
    </div>

    <input type="submit" value="Submit">
  </form>
  <form class="response_form">
   <p>''' +responseLabel+'''</p>
  </form>
  
  </div>
      
  </body>
  </html> 

  '''

if __name__ == '__main__':
  app.run()


