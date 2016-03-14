def to_weird_case(string):
	new_string = []
	for word in string.split():
		new_word = []
		for i in range(len(word)):
			if (i % 2)  == 0:
				new_word.append(word[i].upper())
			else:
				new_word.append(word[i].lower())
		new_string.append("".join(new_word))
	return " ".join(new_string)

print(to_weird_case("Anubhav is a good boy"))
