from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_ngrok import run_with_ngrok

app = Flask(__name__)
run_with_ngrok(app)  # Start ngrok when app is run

#Sample UI
#-------------------------------------------------------------------------------
#
# Enter Set-A                     Enter Set-B
#   -------------------         --------------------
#   |                 |         |                  |
#   -------------------         --------------------
#
#   ------------------------------     
#   | UNION/iNTERSECTION/MINUS    |                OUTPUT
#   ------------------------------               __________________________
#                                                |                         |
#                                                |                         |
#                                                |_________________________| 
#-------------------------------------------------------------------------------

api = Api(app)

setA = set()
setB = set()

#-----------------------------------------------
class SetTheory(Resource):
  def get(self):

    print(request.args)
    operation = int(request.args['operation'])
    setA = set(request.args['setA'].split(','))
    setB = set(request.args['setB'].split(','))

    if (operation == 0):
      print('Union', setA | setB)
      # return {'Union' : list(setA | setB)}, 200
      return home(str(operation),"Union", request.args['setA'], request.args['setB'], str(setA | setB))
    elif (operation == 1):
      print('Intersection', setA & setB)
      return home(str(operation),"Intersection", request.args['setA'], request.args['setB'], str(setA & setB))
      # return {'Intersection' : list(setA & setB)}, 200
    else:
      print('Minus', setA - setB)
      # return {'Minus' : list(setA - setB)}, 200
      return home(str(operation),"Minus", request.args['setA'], request.args['setB'], str(setA - setB))



api.add_resource(SetTheory,"/settheory")

@app.route('/setops', methods=['GET'])
def setOps():

  print(request.args)
  operation = int(request.args['operation'])
  setA = set(request.args['setA'].split(','))
  setB = set(request.args['setB'].split(','))

  if (operation == 0):
      print('Union', setA | setB)
      # return {'Union' : list(setA | setB)}, 200
      return home(str(operation),"Union", request.args['setA'], request.args['setB'], str(setA | setB))
  elif (operation == 1):
      print('Intersection', setA & setB)
      return home(str(operation),"Intersection", request.args['setA'], request.args['setB'], str(setA & setB))
      # return {'Intersection' : list(setA & setB)}, 200
  else:
      print('Minus', setA - setB)
      # return {'Minus' : list(setA - setB)}, 200
      return home(str(operation),"Minus", request.args['setA'], request.args['setB'], str(setA - setB))

#common error handler
@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>Page not found.</p>", 404


@app.route('/', methods=['GET','POST'])
def home(op="0",opName="",setA="1,2,3,4,5", setB="4,5,6,7,8",value=""):
  return '''<!DOCTYPE html>
<html>
<head>
<title>Set Theory</title>
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
<h1>Set Theory</h1>
<p>API Usage : Returns the result of given set and operation</p>
<p class="api_proc">API Call Format : <span>http://localhost:5000/settheory?operation=0&setA=1,2,3,4,4,5,5,5,6,7&setB=1,2,3,3,3,4,5,6,7,9,0</span></p>
</div>
<div class="workarea">

<form action="/setops">
  <label for="message">Operation ( 0 - Union, 1 - Intersection, 2 - Minus)</label><br>
  <input type="text" id="operation" name="operation" value="'''+op+'''"><br>
  <label for="message">Set A ( Comma Seperate Values. Ex= 1,2,3,4,5)</label><br>
  <input type="text" id="setA" name="setA" value="'''+setA+'''"><br>
  <label for="message">Set A ( Comma Seperate Values. Ex= 4,5,6,7,8)</label><br>
  <input type="text" id="setB" name="setB" value="'''+setB+'''"><br>
  <input type="submit" value="Submit">
</form>
<form class="response_form">
  <label for="response">Result of '''+opName+'''</label><br>
  <input type="text" id="response" name="response" value="'''+value+'''"><br>
</form>

</div>
     
</body>
</html> 

'''

if __name__ == '__main__':
  app.run()


