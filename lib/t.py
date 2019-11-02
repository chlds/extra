from datetime import datetime


def t():
	r = datetime.now()
	s = (str(r.hour))
	if(r.minute<(10)): s = (s+(':0'+(str(r.minute))))
	else: s = (s+(':'+(str(r.minute))))
	if(r.second<(10)): s = (s+(':0'+(str(r.second))))
	else: s = (s+(':'+(str(r.second))))
	# s = (s+(' '+(str(r.microsecond))))
	if(__name__==('__main__')):
		print(s)
		return(0x01)
	return(s)


if(__name__==('__main__')): r = t()
