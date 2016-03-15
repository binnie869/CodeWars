from itertools import combinations

def power(s):
	final = []
	temp = []
	for i in range(len(s)+1):
		temp = list(combinations(s,i))
		for item in temp:
			final.append(list(item))

	return final

print(power([1]))


