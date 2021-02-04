<!DOCTYPE html>
<html>

<head>
    <title>Math Log3 Calculator</title>
    <style>
        body {
            background-color: #4db8ff;
            text-align: center;
            color: white;
            font-family: Arial, Helvetica, sans-serif;
        }
        
        .workarea {
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
            width: 10%;
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
$data = 15;
$result = "";

$PI = 3.141592653589793;
function getsin($number)
{
  global $PI;
  $number %= 2 * $PI;
    if ($number < 0) 
        $number = 2 * $PI - $number;
    

    $sign = 1;
    if($number > $PI) {
      
        $number -= $PI;
        $sign = -1;
    }
    

    $PRECISION = 50;
    $temp = 0;
    for ($i=0; $i < $PRECISION + 1; $i++) { 
        $temp += pow(-1, $i) * (pow($number, 2 * $i + 1) / fact(2 * $i + 1));
    }
       
    
    $result = $sign * $temp;
    return $result;
  
}

function getCos($number){
  global $PI;

  $number = ($PI / 2) - $number;
  return getsin($number);
}
    



function fact($num){
  if ($num == 0 || $num == 1)
      return 1;
  else
      return $num * fact($num - 1);
}


if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $opChoice = $_POST['opChoice'];
    $degType = $_POST['degType'];
    $x = $_POST['data'];
    global $PI;
    if ($opChoice <= 5 && $degType == 0)
      $x *= $PI / 180;
    try {
      if ($opChoice == 0) $y = getsin($x); #y = Math.sin(x);
      elseif ($opChoice == 1) $y = getCos($x);
      elseif ($opChoice == 2) $y = getsin($x) / getCos($x);
      elseif ($opChoice == 3) $y = 1 / getsin($x);
      elseif ($opChoice == 4) $y = 1 / getCos($x);
      elseif ($opChoice == 5) $y = getCos($x) / getsin($x);
      elseif ($opChoice == 6) $y = asin($x);
      elseif ($opChoice == 7) $y = acos($x);
      elseif ($opChoice == 8) $y =  atan($x);
      elseif ($opChoice == 9) $y = 1/asin($x);
      elseif ($opChoice == 10)  $y = 1/acos($x);
      else $y = 1/atan($x);
      if ($opChoice >= 6 && $degType == 0) $y *= 180 / $PI;
      $y = round($y, 8);
      $result =  $y;
    }
    catch(Exception $e) {
      $result =  "Infinity";
    }
   
}

?>
    <div class="info">
        <h1>Math Log3 Calculator</h1>
        <p>API Usage : Returns the result of selected log3 trignometry operations</p>

    </div>
    <div class="workarea">
    <form method="post" action="<?php echo htmlspecialchars($_SERVER['PHP_SELF']);?>">
            <select name="opChoice" id="opChoice">
                <!-- <option id="blankOption" selected="true" disabled="disabled" >-- Select an Option --</option> -->
                <option id="sin" selected="true" value="0">sin</option>
                <option id="cos" value="1">cos</option>
                <option id="tan" value="2">tan</option> 
                <option id="cosec" value="3">cosec</option>
                <option id="sec" value="4">sec</option>
                <option id="cot" value="5">cot</option>
                <option id="arcsin" value="6">arcsin</option>
                <option id="arccos" value="7">arccos</option>
                <option id="arctan" value="8">arctan</option>
                <option id="arccosec" value="9">arccosec</option>
                <option id="arcsec" value="10">arcsec</option>
                <option id="arccot" value="11">arccot</option>
            </select>

            <div id="opset1" style="display: inline-block;">
                <label for="data"></label>
                <input type="text" id="data" name="data" value="<?php echo $data; ?>"></br>
            </div>
            <select name="degType" id="degType">
                <option id="deg" value="0" selected="true">deg</option>
                <option id="rad" value="1">rad</option> 
            </select>
            </br>
            <input type="submit" value="Submit">
        </form>
        <form class="response_form">
            <label for="result">Result: </label>
            <input type="text" id="result" name="result" value="<?php echo $result; ?>"></br>
        </form>
    </div>

</body>

</html>