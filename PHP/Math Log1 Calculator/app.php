<!DOCTYPE html>
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
        sub {
            vertical-align: sub;
            font-size: smaller;
        }
    </style>
    
</head>

<?php

$num = 2;
$base = 4;
$num3 = 2;
$data = 3;
$pow = 5;
$result = "";
$OpName = "";


function nLog($x) {
   $n = 99999999;
   return $n * (($x ** (1 / $n)) - 1);
}
    
function clog($x, $base) {
    $result = nLog($x) / nLog($base);
    return $result;
}
   
function antiLog($a,$b){

    $c = 1;
    for ($i=1; $i < $b+1; $i++) { 
      $c = $c * $a;
    }
    return $c;
}

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $opChoice = $_POST['opChoice'];
   
    if ($opChoice == 0){
        $data = $_POST['num3'];
        $base = $_POST['base'];
        $OpName = "Log ";
        $data = '<sub>'.$data.'</sub>'.$base;
        $result = clog($data, $base);
    }
        
    elseif ($opChoice == 1){
        $data = $_POST['num'];
        $result = nLog($data);
        $OpName = "Natural Log ";
    }
        
    elseif($opChoice == 2){
        $data = $_POST['data'];
        $pow = $_POST['pow'];
        $result = antiLog($data, $pow);
        $OpName = "AntiLog  =>";
        $data .= '^'.$pow;
    
    }
        
   

}

?>
<body class="container">
    <div class="row info">
        <h1>Math Log1 Calculator</h1>
        <p>API Usage : Returns the result of selected log1 operations</p>

    </div>

    <div class="workarea">
    <form method="post" action="<?php echo htmlspecialchars($_SERVER['PHP_SELF']);?>">
            <center> <select name="opChoice" id="opChoice" onchange="changeset()">
                <option id="log" value="0" selected='true'>Logarithm(log)</option>
                <option id="nlog" value="1">Natural Logarithm (ln)</option>
                <option id="antilog" value="2"> Anti-logarithm </option>
            </select></center>
            </br>
            <div id="opset1" style="display: block;">
                <label for="data">Enter Number : </label>
                <input type="text" id="num3" name="num3" value="<?php echo $num3; ?>"></br>
                <label for="data">Enter Base : </label>
                <input type="text" id="base" name="base" value="<?php echo $base; ?>"></br>
            </div>

            <div id="opset2" style="display: none;">
                <label for="data">Enter Number:</label>
                <input type="text" id="num" name="num" value="<?php echo $num; ?>"></br>
            </div>
            <div id="opset3" style="display: none;">
                <label for="data">Enter Number:</label>
                <input type="text" id="data" name="data" value="<?php echo $data; ?>"></br>
                <label for="data">Enter Power:</label>
                <input type="text" id="pow" name="pow" value="<?php echo $pow; ?>"></br>
            </div>
            <input type="submit" value="Submit">
        </form>

        <form class="response_form">
            <label for="result"><?php echo $OpName; ?>  <?php echo $data; ?>: </label>
            <input type="text" id="result" name="result" value="<?php echo $result; ?>"></br>

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