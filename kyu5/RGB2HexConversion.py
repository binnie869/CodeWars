def rgb(r, g, b):
	if r >255:
		r = 255
	if r < 0:
		r = 0
	if g > 255:
		g =255
	elif g < 0:
		g = 0
	elif b >255:
		b = 255
	elif b < 0:
		b = 0
	hexr = hex(r).split('x')[1].upper()
	if len(hexr) == 1:
		hexr = "0"+hexr
	hexg = hex(g).split('x')[1].upper()
	if len(hexg) == 1:
		hexg = "0"+hexg
	hexb = hex(b).split('x')[1].upper()
	if len(hexb) == 1:
		hexb = "0"+hexb

	return (hexr+hexg+hexb)


print(rgb(255, 256, 256))