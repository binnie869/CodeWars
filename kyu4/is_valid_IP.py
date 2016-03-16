def is_valid_IP(strng):
	print(strng)
	if len(strng) == 0:
		return False
	sections = strng.split(".")
	if len(sections) != 4:
		return False
	valid  = True
	for section in sections:
		if section.isdigit() == False:
		    return False
		if (int(section) < 0 or int(section) > 255):
		    return False
        if section.startswith('0'):
        	return False
	return valid