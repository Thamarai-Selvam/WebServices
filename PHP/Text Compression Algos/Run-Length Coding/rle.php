<?php
function run_length_encoding($data)
{
    // print("From function");
    // print($data);
    $encoding = "";
    $i = 0;
    // print(strlen($data));
    while ($i < strlen($data))
    {
        $count = 1;
        while (($i + 1) < strlen($data) and $data[$i] == $data[$i+1]){
            $count++;
            $i++;
        }
        $encoding .= strval($count).$data[$i];
        $i++;
        // print($count);
        // print($i);
    }
    // print($encoding);
    return $encoding;
}

$encoding = "5s5r";
$result = "";
$cnt = 0;
$num = "";
$no = array("1", "2", "3", "4", "5", "6", "7", "8", "9", "0");
print(strlen($encoding));
for ($i = 0; $i < strlen($encoding); $i++){
    // print($encoding[$i]);
    if(in_array($encoding[$i],$no)){
        $num .= $encoding[$i];   
    }
    else{
        while($cnt < (int)$num){
            $result = $result.$encoding[$i];
            $cnt++;
        }
        $num = "";
        $cnt = 0;
    }
}

print($result);


?>


