<?php
    $delete = $_POST["delete"];

    $input = file_get_contents('contacts.json');
	$oldFileData = json_decode($input);
	unset($oldFileData[$delete]);
	$oldFileData = array_values($oldFileData);
	$newFileData = json_encode($oldFileData);
	file_put_contents('contacts.json', $newFileData);
    echo "Contact deleted";
?>