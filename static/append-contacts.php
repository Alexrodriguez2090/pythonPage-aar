<?php
    $append = $_POST["append"];

    $input = file_get_contents('contacts.json');
	$oldFileData = json_decode($input);
	$append = json_decode($append);
	array_push($oldFileData, $append);
	$newFileData = json_encode($oldFileData);
	file_put_contents('contacts.json', $newFileData);
    echo "Contact appended";
?>