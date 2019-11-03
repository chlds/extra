def fa(msg):
	print(msg, 'in fa(msg)',end=' ')


def fb(msg):
	print(msg, 'in fb(msg)',end=' ')


def f(fn,arg):
	fn(arg)
	print('..done!')


def main():
	r = 'Hello, Python!'
	f(fb,r)
	f(fa,r)


if(__name__==('__main__')): main()
