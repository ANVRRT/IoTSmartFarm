<?php

$archivo= file_get_contents("RTD.json");
$json_a = json_decode($archivo, true);


//dicc = {'V': {'VS1': ' ','VS2': ' ','VS3': ' ','VS4': ' '} ,
//'H': {'HU1': ' ','HU2': ' ','HU3': ' ','HU4': ' '},
//'T': {'TE1': ' ','TE2': ' ','TE3': ' ','TE4': ' '},
//'L': {'LU1': ' ','LU2': ' ','LU3': ' ','LU4': ' '}}

$V1= $json_a['V']['VS1']; 
$V2= $json_a['V']['VS2']; 
$V3= $json_a['V']['VS3']; 
$V4= $json_a['V']['VS4']; 

$H1= $json_a['H']['HU1']; 
$H2= $json_a['H']['HU2']; 
$H3= $json_a['H']['HU3']; 
$H4= $json_a['H']['HU4']; 

$T1= $json_a['T']['TE1']; 
$T2= $json_a['T']['TE2']; 
$T3= $json_a['T']['TE3']; 
$T4= $json_a['T']['TE4']; 

$L1= $json_a['L']['LU1']; 
$L2= $json_a['L']['LU2']; 
$L3= $json_a['L']['LU3']; 
$L4= $json_a['L']['LU4']; 

if($V1 == "1") $V1 = "Abierto"; 
if($V1 == "0") $V1 = "Cerrado";
if($H1 == "1") $H1 = "Hay humedad"; 
if($H1 == "0") $H1 = "No hay humedad";

if($V2 == "1") $V2 = "Abierto"; 
if($V2 == "0") $V2 = "Cerrado";
if($H2 == "1") $H2 = "Hay humedad"; 
if($H2 == "0") $H2 = "No hay humedad";

if($V3 == "1") $V3 = "Abierto"; 
if($V3 == "0") $V3 = "Cerrado";
if($H3 == "1") $H3 = "Hay humedad"; 
if($H3 == "0") $H3 = "No hay humedad";

if($V4 == "1") $V4 = "Abierto"; 
if($V4 == "0") $V4 = "Cerrado";
if($H4 == "1") $H4 = "Hay humedad"; 
if($H4 == "0") $H4 = "No hay humedad";

?>
<?php include('libraries.php'); ?>	
<div class="container_12">
    <div class="grid_12">
    
        <div class="slogan2">Huerto 1 </div> 
        <div class="slogan2">Estado de la valvula <input type="text" size="50" value="<?php echo $V1?>" readonly></div> 
        <div class="slogan2">Humedad <input type="text" size="50" value="<?php echo $H1?>" readonly></div> 
        <div class="slogan2">Tempertura Valvula <input type="text" size="50" value="<?php echo $T1?>" readonly></div> 
        <div class="slogan2">Luminosidad Valvula <input type="text" size="50" value="<?php echo $L1?>" readonly></div> 

    </div>
    
    <div class="grid_12">
        <div class="slogan2">Huerto 2 </div> 
        <div class="slogan2">Estado de la valvula <input type="text" size="50" value="<?php echo $V2?>" readonly></div> 
        <div class="slogan2">Humedad <input type="text" size="50" value="<?php echo $H2?>" readonly></div> 
        <div class="slogan2">Tempertura <input type="text" size="50" value="<?php echo $T2?>" readonly></div> 
        <div class="slogan2">Luminosidad <input type="text" size="50" value="<?php echo $L2?>" readonly></div> 

    </div>
    
    <div class="grid_12">
        <div class="slogan2">Huerto 3 </div> 
        <div class="slogan2">Estado de la valvula <input type="text" size="50" value="<?php echo $V3?>" readonly></div> 
        <div class="slogan2">Humedad <input type="text" size="50" value="<?php echo $H3?>" readonly></div> 
        <div class="slogan2">Tempertura <input type="text" size="50" value="<?php echo $T3?>" readonly></div> 
        <div class="slogan2">Luminosidad <input type="text" size="50" value="<?php echo $L3?>" readonly></div> 

    </div>
    
    <div class="grid_12">
        <div class="slogan2">Huerto 4 </div> 
        <div class="slogan2">Estado de la valvula <input type="text" size="50" value="<?php echo $V4?>" readonly></div> 
        <div class="slogan2">Humedad <input type="text" size="50" value="<?php echo $H4?>" readonly></div> 
        <div class="slogan2">Tempertura <input type="text" size="50" value="<?php echo $T4?>" readonly></div> 
        <div class="slogan2">Luminosidad <input type="text" size="50" value="<?php echo $L4?>" readonly></div> 

    </div>
</div>

