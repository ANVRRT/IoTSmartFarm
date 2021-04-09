<?php

$V = $_REQUEST['ide'];

$H = $_REQUEST['Hora'];
$F = $_REQUEST['Fecha'];

$B = $_REQUEST['boton'];

system("python3 bfulltables.py '$V' '$H' '$F' '$B'");

?>

