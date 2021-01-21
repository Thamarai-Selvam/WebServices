<!DOCTYPE html>
<html>
<head>
<title>CAPTCHA</title>
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
    $value =  "";$image = "";
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
		$capText = $_POST['value']; 
		$capImage = imagecreatetruecolor(120, 56); 
		$bg = imagecolorallocate($capImage, 245, 245, 237); 
		$fg = imagecolorallocate($capImage, 132, 47, 161); 
		imagefill($capImage, 0, 0, $bg); 
		imagestring($capImage, rand(1, 9), rand(1, 9), rand(1, 9), $capText, $fg); 
		 
		define('Root', dirname(__FILE__));
		$file = Root . $capText . '.png';
		imagepng($capImage,$file);
        if ($capImage) {
        ob_start();
        imagepng($capImage);
        $imgData=ob_get_clean();
        
        $image = '<img src="data:image/png;base64,'.base64_encode($imgData).'" />';

    }
        $value = $capText;
        imagedestroy($capImage);
        
	}
?> 

<div class="info">
<h1>CAPTCHA</h1>
<p>Returns the Image CAPTCHA out of the given message </p>
<p class="api_proc">API Call Format : <span>http://localhost:5000/getcaptcha?value=AWord123</span></p>
</div>
<div class="workarea">

<form method="post" action="<?php echo htmlspecialchars($_SERVER['PHP_SELF']);?>">
  <label for="message">CAPTCHA Content</label><br>
  <input type="text" id="value" name="value" value='<?php echo $value?>'><br>
  <input type="submit" value="Submit">
</form>
<form class="response_form">
  <label for="response">CAPTCHA</label><br>
  <?php echo $image?>
</div>

</body>
</html>