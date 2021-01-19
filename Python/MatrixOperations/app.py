from flask import Flask, request, Response, jsonify,redirect,url_for, render_template_string
from flask_restful import Resource, Api, reqparse
from flask_ngrok import run_with_ngrok
import json

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
#   -------------------------------     
#   | Matrix Ops transpose,ld, etc |             OUTPUT
#   -------------------------------              __________________________
#                                                |                         |
#                                                |                         |
#                                                |_________________________| 
#-------------------------------------------------------------------------------

api = Api(app)


#-----------------------------------------------
class MatOps(Resource):
  def get(self):
    print(request.args)

    operation = int(request.args['op'])
    row = int(request.args['row'])
    col = int(request.args['col'])

    matrix = map(int,request.args['matrix'].split(','))

    tempMat = []
    matrixA = []
    colBkp = col
    for idx,key in enumerate(matrix):
      if (idx < col):
        tempMat.append(key)
      else:
        matrixA.append(tempMat)
        tempMat = [] 
        col += colBkp
        tempMat.append(key)
    matrixA.append(tempMat)

    print('Orgmatrix',matrixA)
    col = colBkp

    if (operation == 0):
      print([[matrixA[j][i] for j in range(len(matrixA))] for i in range(len(matrixA[0]))])
      return self.home(str(operation),'Transpose',str(row), str(col),str(matrixA),str(transpose(matrixA,row,col)))
    elif (operation == 1):
      return self.home(str(operation),'Upper Diagonal',str(row), str(col),str(matrixA),str(upperDiagonal(matrixA,row,col)))
    elif (operation == 2):
      return self.home(str(operation),'Lower Diagonal',str(row), str(col),str(matrixA),str(lowerDiagonal(matrixA,row, col)))
    else:
      return self.home(str(operation),'Swivel',str(row), str(col),str(matrixA),str(swivel(matrixA,row, col)))
    return 'Invalid Request !', 200


  def lowerDiagonal(matrixA, row, col):
    rtempMat = []
    ltempMat = []
    lMatrix = []
    rMatrix = []

    for i in range(0, row):
      for j in range(0, col):
        if (j < i):
          ltempMat.append(matrixA[i][j])
        else:
          ltempMat.append(0)
          
        if (j >= 1) and (i + j > col - 1):
          rtempMat.append(matrixA[i][j])
        else:
          rtempMat.append(0)
      rMatrix.append(rtempMat)
      lMatrix.append(ltempMat)
      rtempMat = []
      ltempMat = []
    
    print(lMatrix)
    print(rMatrix)
      
    return {'OriginalMatrix' : matrixA, 'Lower_Right' : rMatrix, 'Lower_Left' : lMatrix}

    
  def upperDiagonal(matrixA,row, col):
    rtempMat = []
    ltempMat = []
    lMatrix = []
    rMatrix = []
    if row == col:
      for i in range(0, row):
        for j in range(0, col):
          if (j > i):
            rtempMat.append(matrixA[i][j])
          else:
            rtempMat.append(0)
          if (j <= 1) and (i + j < col - 1):
            ltempMat.append(matrixA[i][j])
          else:
            ltempMat.append(0)
        rMatrix.append(rtempMat)
        lMatrix.append(ltempMat)
        rtempMat = []
        ltempMat = []

    return {'OriginalMatrix' : matrixA, 'Upper_Right' : rMatrix, 'Upper_Left': lMatrix}
    

  def transpose(matrixA,row, col):
    rMatrix = [[matrixA[j][i] for j in range(len(matrixA))] for i in range(len(matrixA[0]))] 
    
    return {'OriginalMatrix' : matrixA, 'Tranpose' : rMatrix}
    

  def swivel(matrixA,row,col):

    return {'OriginalMatrix' : matrixA}


  
  @app.route('/', methods=['GET','POST'])
  def home(self='',opType='0',operation='',row='3', col='4',matrix='1,2,3,4,5,6,7,8,9,10,11,12',result=""):
    return render_template_string('''<!DOCTYPE html>
    <html>
    <head>
    <title>Matrix Operations</title>
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

      <form action="/matops">
        <label for="op">Operation </br> (0 - Transpose, 1 - Upper Diagonal Left & Right, 2 - Upper Diagonal Left & Right, 3 - Swivel)</label><br>
        <input type="text" id="op" name="op" value="'''+opType+'''"><br>
        <label for="row">Rows</label><br>
        <input type="text" id="row" name="row" value="'''+row+'''"><br>
        <label for="col">Columns</label><br>
        <input type="text" id="col" name="col" value="'''+col+'''"><br>
        <label for="matrix">Matrix </br>(Comma seperated values. Ex. 1,2,3,4,5,6,7,8,9,0,1,2,3,4,5)</label><br>
        <textarea type="text" id="matrix" name="matrix" rows="4" cols="50" >'''+matrix+'''</textarea>
        <br>
        <input type="submit" value="Submit">
      </form>
      <form class="response_form">
        <label for="response">Result of '''+operation+'''</label><br>
        <textarea id="response" name="response" rows="4" cols="50" >'''+result+'''</textarea>
      </form>
    </div>
        
    </body>
    </html> 

    ''')

  @app.errorhandler(404)
  def page_not_found(e):
      return "<h1>404</h1><p>Page not found.</p>", 404

  
api.add_resource(MatOps, '/matops')

if __name__ == '__main__':
  app.run()
