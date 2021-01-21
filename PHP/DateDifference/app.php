<!DOCTYPE html>
<html>
<head>
<title>Date Difference</title>
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
.err_proc {
            background-color: red;
            padding: 7px;
            border-radius: 20px;
        }
.workarea {
text-align : left;
padding : 50px;
}

input[type=text] {
  width:15%;
  padding: 12px 10px;
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
    <?php
     $fromDate = 12; $fromMonth = 10; $fromYear = 2020; $fromHour = 10; $fromMinute = 44; $fromSeconds = 30;
     $toDate = 10; $toMonth = 8; $toYear = 2020; $toHour = 11; $toMinute = 32; $toSeconds = 21;
     $diff = "";
     if ($_SERVER["REQUEST_METHOD"] == "POST") {
        // collect value of input field
        $fromDate = $_POST['fromDate']; $fromMonth = $_POST['fromMonth']; $fromYear = $_POST['fromYear']; $fromHour = $_POST['fromHour']; $fromMinute = $_POST['fromMinute']; $fromSeconds = $_POST['fromSeconds'];
        $toDate = $_POST['toDate']; $toMonth = $_POST['toMonth']; $toYear = $_POST['toYear']; $toHour = $_POST['toHour']; $toMinute = $_POST['toMinute']; $toSeconds = $_POST['toSeconds'];
        
        
        $fromPeriod = date_create($fromYear.'-'.$fromMonth.'-'.$fromDate.' '.$fromHour.':'.$fromMinute.':'.$fromSeconds);
        $toPeriod = date_create($toYear.'-'.$toMonth.'-'.$toDate.' '.$toHour.':'.$toMinute.':'.$toSeconds);
        
       
        // send the result now
        if (empty($fromPeriod) || empty($toPeriod)) {
            echo "<p class='err_proc'>Invalid Date Format</p>";
        } else {
             $diff= date_diff($toPeriod,$fromPeriod);
            // echo date_format($fromPeriod,"Y/m/d H:iP");
            // echo date_format($toPeriod,"Y/m/d H:iP");
             $diff = $diff->format('%y Years %m Months %d Days %h Hours %i Minutes %s Seconds');
        }
    }
    
    
    ?>
<div class="info">
<h1>Date Difference</h1>
<p>API Usage : Returns the difference b/w two given dates</p>
<p class="api_proc">API Call Format : <span>http://localhost:5000/datediff?fromYear=2020&fromMonth=07&fromDate=15&fromHour=0&fromMinute=1&fromSeconds=1&toYear=2020&toMonth=09&toDate=30&toHour=0&toMinute=10&toSeconds=1</span></p>
</div>
<div class="workarea">


<form method="post" action="<?php echo htmlspecialchars($_SERVER['PHP_SELF']);?>">
    <label for="fromDate">From Date Time</label><br>
<div id="fromBlock" name="fromBlock">
    <label for="fromYear">Year</label>
    <input type="text" id="fromYear" name="fromYear" value='<?php echo $fromYear?>'>
    <label for="fromMonth">Month</label>
    <input type="text" id="fromMonth" name="fromMonth" value='<?php echo $fromMonth?>'>
    <label for="fromDate">Date</label> 
    <input type="text" id="fromDate" name="fromDate" value='<?php echo $fromDate?>'>
    <br>
    <label for="fromHour">Hour</label>
    <input type="text" id="fromHour" name="fromHour" value='<?php echo $fromHour?>'>
    <label for="fromMinute">Minute</label>
    <input type="text" id="fromMinute" name="fromMinute" value='<?php echo $fromMinute?>'>
    <label for="fromSeconds">Seconds</label>
    <input type="text" id="fromSeconds" name="fromSeconds" value='<?php echo $fromSeconds?>'>
    </div><br>
    <label for="toBlock">To Date Time</label><br>
    <div id="toBlock" name="toBlock">
    
    <label for="toYear">Year</label>
    <input type="text" id="toYear" name="toYear" value='<?php echo $toYear?>'>
    <label for="toMonth">Month</label>
    <input type="text" id="toMonth" name="toMonth" value='<?php echo $toMonth?>'>
    <label for="toDate">Date</label>
    <input type="text" id="toDate" name="toDate" value='<?php echo $toDate?>'>
    <br>
    <label for="toHour">Hour</label>
    <input type="text" id="toHour" name="toHour" value='<?php echo $toHour?>'>
    <label for="toMinute">Minute</label>
    <input type="text" id="toMinute" name="toMinute" value='<?php echo $toMinute?>'>
    <label for="toSeconds">Seconds</label>
    <input type="text" id="toSeconds" name="toSeconds" value='<?php echo $toSeconds?>'>
    </div>

    <input type="submit" value="Submit">
  </form>
  <form class="response_form">
   <p><?php echo $diff?></p>
  </form>
  
  </div>
      
  </body>
  </html> 
