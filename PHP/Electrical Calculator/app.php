<!DOCTYPE html>
<html>

<head>
    <title>Electrical Calculator</title>
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
    $w = $kw = $mw = "";
    $num = 10; $num1 = 12;
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $vChoice = $_POST['vChoice'];
        $aChoice =  $_POST['aChoice'];
        $a =  $_POST['num'];
        $v =  $_POST['num1'];



        if ($aChoice == 0)
            $a /= 1000;
        else if ($aChoice == 1)
            $a = $a;
        else
            $a *= 1000;
        if ($vChoice == 0)
            $v /= 1000;
        else if ($vChoice == 1)
            $v = $v;
        else
            $v *= 1000;

        $w = $a * $v;
        $kw = $a * $v / 1000;
        $mw = $a * $v * 1000;
                
    }
?> 
    <div class="info">
        <h1>Electrical Calculator</h1>
        <p>API Usage : Returns the result of selected electrical unit operations</p>

    </div>

    <div class="workarea">
    <form method="post" action="<?php echo htmlspecialchars($_SERVER['PHP_SELF']);?>">

            </br>
            <div id="opset1" style="display: block;">
                <label for="data">Enter Current in amps : </label></br>
                <input type="text" id="num" name="num" value="<?php echo $num?>">
                <select name="aChoice" id="opChoice">
                    <option id="ma" value="0">mA</option>
                    <option id="a" selected="true" value="1">A</option>
                    <option id="ka" value="2">kA</option>
                    </select></br>
                <label for="data">Enter Current in volts   : </label></br>
                <input type="text" id="num1" name="num1" value="<?php echo $num1?>">
                <select name="vChoice" id="opChoice">
                    <option id="mv"  value="0">mv</option>
                    <option id="v" selected="true"value="1">V</option>
                    <option id="kv" value="2">kV</option>

                </select></br>
            </div>


            <input type="submit" value="Submit">
        </form>

        <form class="response_form">
            <label for="kw">Power result in kilowatts: </label></br>
            <input type="text" id="kw" name="kw" value="<?php echo $kw?>"></br>
            <label for="w">Power result in watts: </label></br>
            <input type="text" id="w" name="w" value="<?php echo $w?>"></br>
            <label for="mw">Power result in milliwatts: </label></br>
            <input type="text" id="mw" name="mw" value="<?php echo $mw?>"></br>

        </form>
    </div>

</body>

</html>