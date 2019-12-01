<?php
    $updatenum = $_POST["updatenum"];
    $updatecon = $_POST["updatecon"];

    $input = file_get_contents('contacts.json');
	$oldFileData = json_decode($input);
	$updatecon = json_decode($updatecon);
	$oldFileData[$updatenum] = $updatecon;
	$oldFileData = array_values($oldFileData);
	$newFileData = json_encode($oldFileData);
	file_put_contents('contacts.json', $newFileData);
    echo "Contact updated";
?>