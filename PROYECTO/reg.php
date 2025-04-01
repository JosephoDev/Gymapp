<?php
$link = mysqli_connect("localhost","root","","mydb") or die("<h2>Error no se cuentra la base de datos</h2> " . mysqli_error($link));
$db = mysqli_select_db($link, "mydb") or die("Error " . mysqli_error($link));



?>