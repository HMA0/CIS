<?php

$my_file = fopen("location.txt", "w");
$information = "lat:" . $_GET["lat"] . "\nlong:" . $_GET["long"] . "\nip: " . $_SERVER["REMOT_ADDER"];
fwrite($my_file, $information);
fclose($my_file);


?>
