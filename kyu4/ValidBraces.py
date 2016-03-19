def validBraces(string):
	counter_par = 0
	counter_brackets = 0
	counter_braces = 0
	for letter in string:
		if letter == "(":
			counter_par +=1
		if letter == ")":
			if counter_par == 0:
				return False
			counter_par -=1
		if letter == "[":
			counter_brackets +=1
		if letter == "]":
			if counter_brackets == 0:
				return False
			counter_brackets -=1
		if letter == "{":
			counter_braces +=1
		if letter == "}":
			if counter_braces == 0:
				return False
			counter_braces -=1
	if counter_par ==0 and counter_brackets == 0 and counter_braces ==0:
		return True
	else:
		return False