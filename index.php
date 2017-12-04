<?php

$command = escapeshellcmd('scraper.py 106601');
$output = shell_exec($command);
echo $output;

?>
