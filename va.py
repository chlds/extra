def va(arg0,arg1,*args,**kwargs):
	print(arg0,len(arg0))
	print(arg1,len(arg1))
	print(args,len(args))
	print(kwargs,len(kwargs))
	return(0x01)


def main():
	r = va('Variable','Arguments',0,1,2,3,'Hello, Python!',name='Python',email='python@example.com',star=5,notes='',)
	print(r)


if(__name__==('__main__')): main()
