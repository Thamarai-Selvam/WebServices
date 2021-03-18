<?php
$com = "66,65,256,257,65,260";
$com = explode(",",$com);
$i;$w;$k;$result;
$dictionary = array();
$entry = "";
$dictSize = 256;
for ($i = 0; $i < 256; $i++) {
    $dictionary[$i] = chr($i);
}
$w = chr($com[0]);
$result = $w;
for ($i = 1; $i < count($com);$i++) {
    $k = $com[$i];
    if ($dictionary[$k]) {
        $entry = $dictionary[$k];
    } else {
        if ($k === $dictSize) {
            $entry = $w.$w[0];
        } else {
            return null;
        }
    }
    print($dictionary[256]);
    $result .= $entry;
    $dictionary[$dictSize++] = $w . $entry[0];
    $w = $entry;
}
print($result)
?>