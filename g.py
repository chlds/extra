def fn():
	global r # i.e., extern r; // expressed in C
	print(r)
	r = (0x01)


r = (0x10)
fn()
print(r)
