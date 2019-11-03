def fa(msg):
	print(msg, 'in fa(msg)',end=' ')


def fb(msg):
	print(msg, 'in fb(msg)',end=' ')


def f(fn,arg):
	fn(arg)
	print('..done!')


def main():
	r = 'Hello, Python!'
	nm = ['fn. A','fn. B',]
	ls = [fa,fb,]
	m = 'fn. B'
	if m in nm:
		i = nm.index(m)
		f(ls[i],r)
		ls[i](r)


if(__name__==('__main__')): main()
