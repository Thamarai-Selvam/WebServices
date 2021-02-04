<!DOCTYPE html>
<html>
<head>
<title>QRCode</title>
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
    $value = "Message";
    $isrc = " ";
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $value = $_POST['value'];
       
        $isrc = 'https://chart.googleapis.com/chart?chs=100x100&cht=qr&chl='.$value;

    }
?>


<div class="info">
<h1>QRCode</h1>
<p>Returns the Image QRCode out of the given message </p>
<p class="api_proc">API Call Format : <span>http://localhost:5000/qrcode?value=AWord123</span></p>
</div>
<div class="workarea">

<form method="post" action="<?php echo htmlspecialchars($_SERVER['PHP_SELF']);?>">
  <label for="message">QRCode Content</label><br>
  <input type="text" id="value" name="value" value="<?php echo $value; ?>"><br>
  <input type="submit" value="Submit">
</form>
<form class="response_form">
  <label for="response">QRcode</label><br>
  <img src="<?php echo $isrc; ?>"></img>
</form>
</div>

</body>
</html>