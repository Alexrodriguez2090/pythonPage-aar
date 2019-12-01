<?php
    header("Content-Type: application/json; charset=UTF-8");
    $myfiler = fopen("{{ url_for('static', filename='contacts.json') }}", "r") or die("Unable to open file to read!");
    $obj = fread($myfiler,filesize("{{ url_for('static', filename='contacts.json') }}"));
    fclose($myfiler);
    echo $obj;
?>