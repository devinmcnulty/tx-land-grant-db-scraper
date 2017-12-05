<?php
$id = $_SERVER['QUERY_STRING'];
$output = shell_exec("sudo -u root -S python3 scraper.py $id"); 
header("Location: $output");
exit();

?>
