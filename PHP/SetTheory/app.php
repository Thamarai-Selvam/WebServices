<!DOCTYPE html>
<html><head>
    <title>Set Theory</title>
    <style>
        body {
            background-color: #4db8ff;
            text-align: center;
            color: white;
            font-family: Arial, Helvetica, sans-serif;
        }
        
        span {
            color: white;
            font-style: oblique;
        }
        
        .info {
            background-color: #0099ff;
            padding: 20px;
            margin: -10px -10px 0 -10px;
        }
        
        .err_proc {
            background-color: red;
            padding: 7px;
            border-radius: 20px;
        }
        .api_proc {
            background-color: #6600cc;
            padding: 7px;
            border-radius: 20px;
        }
        
        .workarea {
            text-align: left;
            padding: 50px;
        }
        
        input[type=text] {
            width: 80%;
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
    $operation = "1";
    $setA = "1,2,3,4,5";
    $setB = "4,5,6,7,8";
    $operName = "";
    $resultSet = ""; 
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $operation = $_POST['operation'];
        $setA = $_POST['setA'];
        $setB = $_POST['setB'];
        $Aset = array();
        $Bset = array();
        if (empty($operation)) {
            echo "<p class='err_proc'>Invalid Operation</p>";
        }
        elseif (empty($setA)){
            echo "<p class='err_proc'>Invalid Set A</p>";
        }elseif (empty($setB)){
            echo "<p class='err_proc'>Invalid Set B</p>";
        }else{
            $Aset = explode(',',$setA);
            $Bset = explode(',',$setB);
        }

        if($operation == 1){
            $operName = "Union";
            $resultSet = implode(',', (array_merge($Aset, $Bset)));
        } elseif($operation == 2){
            $operName = "Intersection";
            $resultSet = implode(',', (array_intersect($Aset, $Bset)));
        }elseif($operation == 3){
            $operName = "Minus";
            $resultSet = implode(',', (array_diff($Aset, $Bset)));
        }
        else{
            echo "<p class='err_proc'>Something went wrong !</p>";
        }
        
        }
        
?>


    <div class="info">
        <h1>Set Theory</h1>
        <p>Returns the result of the given operation on sets</p>
        <p class="api_proc">API Call Format : <span>http://localhost:5000/settheory?operation=0&setA=1,2,3,4,4,5,5,5,6,7&setB=1,2,3,3,3,4,5,6,7,9,0</span></p>
    </div>
    <div class="workarea">

        <form method="post" action="<?php echo htmlspecialchars($_SERVER['PHP_SELF']);?>">
            <label for="message">Operation ( 1 - Union, 2 - Intersection, 3 - Minus)</label><br>
            <input type="text" id="operation" name="operation" value='<?php echo $operation ?>'><br>
            <label for="message">Set A ( Comma Seperate Values. Ex= 1,2,3,4,5)</label><br>
            <input type="text" id="setA" name="setA" value='<?php echo $setA ?>'><br>
            <label for="message">Set A ( Comma Seperate Values. Ex= 4,5,6,7,8)</label><br>
            <input type="text" id="setB" name="setB" value='<?php echo $setB ?>'><br>
            <input type="submit" value="Submit">
            </form>
            <form class="response_form">
            <label for="response">Result of <?php echo $operName ?></label><br>
            <input type="text" id="response" name="response" value='<?php echo $resultSet ?>'><br>
        </form>

    </div>

</body>
</html>