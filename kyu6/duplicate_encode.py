from collections import defaultdict

def duplicate_encode(word):
	new_word =[]
	word_dict = defaultdict(int)
	for letter in word.lower():
		word_dict[letter] +=1
	for letter in word.lower():
		if word_dict[letter] == 1:
			new_word.append("(")
		else:
			new_word.append(")")

	return "".join(new_word)