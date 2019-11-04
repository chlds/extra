DBG = (0x00)


def check(arg):
	VO = 'Show me'
	O = ['all the channels','all the members','all the permissions',]
	len_objs = len(O)
	if(DBG): print('Length of objects:',str(len_objs))
	NAME = 'Python'
	REQ = [f'{VO} {O[0]}, {NAME}',f'{VO} {O[1]}, {NAME}',f'{VO} {O[2]}, {NAME}',]
	if arg in REQ:
		r = REQ.index(arg)
		return(r)
	else: return('Oops..')


def main():
	content = 'Show me all the permissions, Python'
	r = check(content)
	print(content,': index',r)
	content = 'Show me all the permissions, Python!'
	r = check(content)
	print(content,': index',r)


if(__name__==('__main__')): main()
