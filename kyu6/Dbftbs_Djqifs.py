def encryptor(key, message):
	lower = [letter.islower() for letter in message]
	new_message = []
	while (key <= -26):
		key = key+26
	if key < 0:
		key = 26 + key
	while key>=26:
		key = key-26
	for letter in message.upper():
		if letter.isalpha():
			if (ord(letter)+key) > 90:
				new_message.append(chr(ord('A')+((ord(letter)+key) - 91)))
			else:
				new_message.append(chr(ord(letter)+key))
		else:
			new_message.append(letter)
	
	for i in range(len(new_message)):
		if lower[i] == True:
			new_message[i] = new_message[i].lower()
	return "".join(new_message)

print(encryptor(13, 'Caesar Cipher'))
print(encryptor(-5, 'Hello World!'))