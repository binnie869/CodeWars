def unique_in_order(iterable):
    if len(iterable) < 2:
    	return list(iterable)
    new_iterable = []
    new_iterable.append(iterable[0])
    for i in range(1, len(iterable)):
        if iterable[i] == iterable[i-1]:
        	continue
        new_iterable.append(iterable[i])
    return new_iterable