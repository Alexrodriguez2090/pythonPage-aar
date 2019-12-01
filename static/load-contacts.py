<?py
    header("Content-Type: application/json; charset=UTF-8");
    file_name = "{{ urlfor('static', filename='contacts.json' }}";
    instructionsFile = open(file_name,"r");
    instructionsFile.close();
    if instructionsFile == '':
    	instructionsFile = 1
	else:
		pass
    print(instructionsFile);
?>