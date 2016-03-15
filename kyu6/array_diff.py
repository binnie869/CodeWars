def array_diff(a, b):
	new_a = list(a)
	for item in set(b):
		for val in a:
			if val == item:
				new_a.remove(val)
	return new_a