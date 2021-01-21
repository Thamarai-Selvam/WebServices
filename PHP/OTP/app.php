<!DOCTYPE html>
<html><head>
    <title>OTP</title>
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
    $typeContent = "";
    $length = "6";
    $otpType = "2";
    $otpContent = ""; 
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $length = $_POST['length'];
        $otpType = $_POST['typeotp'];
        
        if (empty($length)) {
            echo "<p class='err_proc'>Invalid Length</p>";
        }
        if($otpType == 0){
            $typeContent = "1234567890";
        } elseif($otpType == 1){
            $typeContent = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
        }elseif($otpType == 2){
            $typeContent = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
        }
        

        if (empty($typeContent)) {
            echo "<p class='err_proc'>Invalid Type</p>";
        }
        else{
            for ($i = 1; $i <= $length; $i++) { 
                $otpContent .= substr($typeContent, (rand()%(strlen($typeContent))), 1); 
            }
        }
        
        

    }
?>


    <div class="info">
        <h1>OTP</h1>
        <p>Returns the OTP of desired length</p>
        <p class="api_proc">API Call Format : <span>http://localhost:5000/otp?length=4&typeotp=</span></p>
    </div>
    <div class="workarea">
        <form method="post" action="<?php echo htmlspecialchars($_SERVER['PHP_SELF']);?>">
            <label for="message">OTP Length</label><br>
            <input type="text" id="length" name="length" value='<?php echo $length; ?>'><br>
            <label for="message">Type( 0 - Numeric, 1 - Alphabets, 2 - Alphanumeric)</label><br>
            <input type="text" id="typeotp" name="typeotp" value='<?php echo $otpType; ?>'><br>
            <input type="submit" value="Submit">
        </form>
        <form class='response_form'>
           <label for='response'>OTP</label><br>
           <input type='text' id='response' name='response' value='<?php echo $otpContent; ?>'>
           <br>
         </form>
    </div>

</body>
</html>