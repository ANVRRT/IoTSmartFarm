<?php
//$_POST['IB1'];
$V = $_REQUEST['IB1'];
//echo $_POST['boton'];
$B = $_REQUEST['boton'];

system("python3 Botones.py '$V' '$B'");

?>
