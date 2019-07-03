<?php
$hash_key = "kinda_safe_string:D";
$hash = md5($_GET['id'] . $hash_key);
echo $hash;
?>