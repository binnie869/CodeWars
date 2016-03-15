def find_nb(m):
	i =	2
	print(i**3)
	area = 1
	while area < m:
		area += i**3
		# print(area, m)
		if area == m:
			return i
		i += 1
	return -1

print(find_nb(4183059834009))