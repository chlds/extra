from datetime import datetime


def d():
	month = ['','January','February','March','April','May','Jane','July','August','September','October','November','December']
	week = ['Mon.','Tue.','Wed.','Thu.','Fri.','Sat.','Sun.']
	r = datetime.now()
	w = r.weekday()
	s = (str(week[w]))
	s = (s+(' '+(str(r.day))))
	s = (s+(' '+(month[r.month])))
	s = (s+(' '+(str(r.year))))
	if(__name__==('__main__')):
		print(s)
		return(0x01)
	return(s)


if(__name__==('__main__')): r = d()
