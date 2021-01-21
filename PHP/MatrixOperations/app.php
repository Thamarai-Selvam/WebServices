<!DOCTYPE html>
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
    <h1>Matrix Operations</h1>
    <p>API Usage : Returns the result of given matrix and operation</p>
    <p class="api_proc">API Call Format : <span>http://localhost:5000/matops?op=0&row=3&col=5&matrix=1,2,3,4,5,6,7,8,9,0,1,2,3,4,5</span></p>
    </div>
    <div class="workarea">

      <form action="/matops">
        <label for="op">Operation </br> (0 - Transpose, 1 - Upper Diagonal Left & Right, 2 - Lower Diagonal Left & Right, 3 - Swivel)</label><br>
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
