<!DOCTYPE html>
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
<?php
 $data = $data1 = $data2 = $result = '';

 
function Variance($data){
    $n = count($data);
    $mean = array_sum($data) / $n;
    // $deviations = [( x- mean) **2 for x in data];
    $variance = 0.0;
    foreach($data as $i) 
    { 
        $variance += pow(($i - $mean), 2); 
    } 
    
    return $variance/$n;
}


function stdDev($data){
     return  sqrt(Variance($data));
}
   

function lrReg($X, $Y){
    $sumX = array_sum($X);
    $sumY = array_sum($Y);
    $sumXX = 0;
    $sumXY = 0;
    for ($i=0; $i < count($X); $i++) { 
        $sumXX += $X[$i] * $X[$i];
        $sumXY += $X[$i] * $Y[$i];
    }




$n = count($X);

$a = (($sumY * $sumXX) - ($sumX * $sumXY)) / (($n * $sumXX) - ($sumX * $sumX));
$b = (($n * $sumXY) - ($sumX * $sumY)) / (($n * $sumXX) - ($sumX * $sumX));

# REGRESSION EQUATION = > Y = a + bx
return "{$a} + {$b}(x)";
}
if ($_SERVER["REQUEST_METHOD"] == "POST") {


    $opChoice = $_POST['opChoice'];
    
   
    if ($opChoice == 0) {
        $data =  explode(",",$_POST['data']);
        $result = stdDev($data);
        $data = $_POST['data'];
    }
    elseif ($opChoice == 1) {
        $data =  explode(",",$_POST['data']);
        $result = Variance($data);
        $data = $_POST['data'];
    }
       
    else {
        $data1 =  explode(",",$_POST['data1']);
        $data2 = explode(",",$_POST['data2']);
        $result = lrReg($data1, $data2);
        
    }
        
    
    
}


?>
<div class="info">
<h1> Statistics calculator </h1>
</div>
 <div class="workarea">
 <form method="post" action="<?php echo htmlspecialchars($_SERVER['PHP_SELF']);?>">
            <center> <select name="opChoice" id="opChoice" onchange="changeset()">
                <option id="stdev" value="0" selected='true'>Standard Deviation</option>
                <option id="variance" value="1">Variance</option>
                <option id="lreg" value="2">Linear Regression</option>
            </select></center>
            </br>

            <div id="opset1" style="display: block;">
                <label for="data">Enter the data (Ex. 2,4,6,8):</label>
                <input type="text" id="data" name="data" value="<?php echo $data; ?>"></br>
            </div>
            <div id="opset2" style="display: none;">
                <label for="data">Enter X set  (Ex. 2,4,6,8): </label>
                <input type="text" id="data1" name="data1" value="<?php echo $data1; ?>"></br>
                <label for="data1">Enter Y set (Ex. 2,4,6,8): </label>
                <input type="text" id="data2" name="data2" value="<?php echo $data2; ?>"></br>
            </div>
            <input type="submit" value="Submit">
        </form>

        <form class="response_form">
            <label for="result">Result</label>
            <input type="text" id="result" name="result" value="<?php echo $result; ?>"></br>

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
