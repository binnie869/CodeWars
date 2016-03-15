def valid_parentheses(string):
	counter = 0:
	for letter in string:
		if letter == "(":
			counter +=1
		elif letter == ")":
			if counter == 0:
				return False
			counter -=1
		else:
			continue
	if counter != 0:
		return False
	else:
		return True