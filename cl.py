class Cl:
	def fa(self,arg):
		print(arg,'in fa(self,arg)')
	def fb(self,arg):
		print(arg,'in fb(self,arg)')


def main():
	r = 'Hello, Python!'
	c = Cl() # map on the RAM
	d = Cl() # map
	e = d # point i.e., not map
	print(Cl)
	print(c)
	print(d)
	print(e)
	c.fa(r)
	c.fb(r)
	d.fa(r)
	e.fa(r)


if(__name__==('__main__')): main()
