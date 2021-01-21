<!DOCTYPE html>
<html><head>
    <title>FigureToCurrency</title>
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
    function console_log($output, $with_script_tags = true) {
        $js_code = 'console.log(' . json_encode($output, JSON_HEX_TAG) . ');';
        if ($with_script_tags) {
            $js_code = '<script>' . $js_code . '</script>';
        }
        echo $js_code;
    }
    $number = "3450";
    $words = "";
    $flag = 0;
    $a = array("", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty", '30'=>"thirty", '40'=>"forty", '50'=>"fifty", '60'=>"sixty", '70'=>"seventy", '80'=>"eighty", '80'=>"ninety");
    $levels = array(" ", "hundred ", "thousand ", "lakh ", "crore ");

    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $number = $numBkp = $_POST['value'];
        
        if (empty($number)) {
            echo "<p class='err_proc'>Invalid Figure</p>";
            $flag = 1;
        }
        else {
            $noOfDigits = strlen($number);
            console_log('Dnum'.$noOfDigits); 
            console_log('num'.$number); 
            
            $digitsLeft = 0;
            $cValue = array();
            if ($noOfDigits > 9)  {
                echo "<p class='err_proc'>Overflow !</p>";
                $flag = 1;
            }
            else{
               while( $digitsLeft < $noOfDigits){

                $curNum = floor($number % (($digitsLeft == 2) ? 10 : 100));
                $number = floor($number / (($digitsLeft == 2) ? 10 : 100));
            
                if($curNum){
                    $level = count($cValue);
                    $cValue [] = ($curNum < 20) ? $a[$curNum].' '.$levels[$level] : $a[floor($curNum / 10) * 10].' '.$a[$curNum % 10].' '.$levels[$level];
                }
                else $cValue[] = null;
               
                $digitsLeft += (($digitsLeft == 2) ? 10 : 100) == 10 ? 1 : 2;
            }
                $words = implode('', array_reverse($cValue));
                $number = $numBkp; 
            }
            }
             

        if (empty($words) && $flag != 1) {
            echo "<p class='err_proc'>Something Went Wrong !</p>".$words;
        }
    }
?>


   
<div class="info">
<h1>Figures to Currency</h1>
<p>API Usage : Returns the words of given number value</p>
<p class="api_proc">API Call Format : <span>http://localhost:5000/currency?value=5001</span></p>
</div>
<div class="workarea">

<form method="post" action="<?php echo htmlspecialchars($_SERVER['PHP_SELF']);?>">
  <label for="message">Figures</label><br>
  <input type="text" id="value" name="value" value='<?php echo $number?>'><br>
  <input type="submit" value="Submit">
</form>
<form class="response_form">
  <label for="response">Words</label><br>
  <input type="text" id="response" name="response" value='<?php echo $words?>'><br>
</form>
</div>

</body>
</html>