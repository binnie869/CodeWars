def zeros(n):
	twos = 0
	fives = 0
	for i in range(1, n+1):
		while i%2 == 0:
			twos +=1
			i /= 2
	for i in range(1, n+1):
		while i%5 == 0:
			fives +=1
			i /= 5
	if fives < twos	:
		return fives
	else:
		return twos
