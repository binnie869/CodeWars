def to_camel_case(text):
	camel_case = []
	upper = False
	for letter in text:
		if letter  != "-" and letter != "_":
			if upper == True:
				camel_case.append(letter.upper())
				upper = False
			else:
				camel_case.append(letter)
		else:
			upper = True

	return "".join(camel_case)
