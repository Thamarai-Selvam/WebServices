<!DOCTYPE html>
<html>

<head>
    <title>Math Log2 Calculator</title>
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

<body>
<?php

$num = 2;
$num3 = 2;
$data = 3;
$pow = 5;
$result = "";
$OpName = "";


function rgcf($x, $y) {
    if ($x == 0)
        return $y;
    return rgcf($y % $x, $x);
}

  


function gcf($data) {
    $tempRes = $data[0];

    foreach($data as $element)
        $tempRes = rgcf($element, $tempRes);
    if($tempRes == 1)
        return 1;
    return $tempRes;
}




function rlcm($x, $y) {

    if(!$x || !$y)
        return 0;
    else
        return abs(($x * $y) / rgcf($x, $y));
    
}



function lcm($data) {
    $tempRes = $data[0];

    foreach($data as $element)
        $tempRes = rlcm($element, $tempRes);
    if($tempRes == 1)
        return 1;
    return $tempRes;
}




if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $opChoice = $_POST['opChoice'];
   
    if ($opChoice == 0){
        $data = explode(",",$_POST['data']);

        $OpName = "GCF and LCM of ";
        $result = gcf($data)." and ".lcm($data);
        $data = $_POST['data'];
    }
        
    elseif ($opChoice == 1){
        $data =  $_POST['num'];

        $result = $data**(1/2).' and '.$data**(1/3);
        $OpName = "Square Root and Cube Root of ";
    }
        

    elseif ($opChoice == 2){
        $data =$_POST['num3'];
        $pow = $_POST['pow'];
        $result = $data**(1/$pow);

        $OpName = '<sup>'.$pow.'</sup>√'.$data;
        $pow = $data = '';
    }
       

        
}

?>
    <div class="info">
        <h1>Math Log2 Calculator</h1>
        <p>API Usage : Returns the result of selected log2 operations</p>

    </div>
    <div class="workarea">
    <form method="post" action="<?php echo htmlspecialchars($_SERVER['PHP_SELF']);?>">
            <center> <select name="opChoice" id="opChoice" onchange="changeset()">
                <option id="gcflcm" value="0" selected="true">GCF and LCM</option>
                <option id="sqcrt" value="1">Square and Cube Root</option>
                <option id="nrt" value="2">N<sup>th</sup> Root</option>
            </select></center>
            </br>

            <div id="opset1" style="display: block;">
                <label for="data">Enter the data (Ex. 2,4,6,8):</label>
                <input type="text" id="data" name="data" value="<?php echo $data; ?>"></br>
            </div>
            <div id="opset2" style="display: none;">
                <label for="data">Enter Number:</label>
                <input type="text" id="num" name="num" value="<?php echo $num; ?>"></br>
            </div>
            <div id="opset3" style="display: none;">
                <label for="data">Enter Number : </label>
                <input type="text" id="num3" name="num3" value="<?php echo $num3; ?>"></br>
                <label for="data">Enter Root : </label>
                <input type="text" id="pow" name="pow" value="<?php echo $pow; ?>"></br>
            </div>
            <input type="submit" value="Submit">
        </form>

        <form class="response_form">
            <label for="result"><?php echo $OpName; ?> <?php echo $data; ?> : </label>
            <input type="text" id="result" name="result" value="<?php echo $result; ?>"</br>

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