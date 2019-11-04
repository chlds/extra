DBG = (0x00)


def check(arg):
	VO = 'Show me'
	O = ['all the channels','all the members','all the permissions',]
	NAME = 'Python'
	objs = len(O)
	if(DBG): print('Length of objects:',str(objs))
	REQ = []
	for n in range(objs):
		s = f'{VO} {O[n]}, {NAME}'
		REQ.append(s)
	if(DBG): print(REQ)
	if arg in REQ:
		r = REQ.index(arg)
		return(r)
	else: return('Oops..')


def main():
	msg = 'Show me all the permissions, Python'
	r = check(msg)
	print(msg,': index',r)
	msg = 'Show me all the permissions, Python!'
	r = check(msg)
	print(msg,': index',r)


if(__name__==('__main__')): main()
