<?php
$id = $_SERVER['QUERY_STRING'];
$output = shell_exec("sudo -u root -S python3 request_url.py $id");
header("Location: $output");
exit();

?>
