import sys

argv = (sys.argv)
argc = len(argv)

# print('argc: '+(str(type(argc))))
# print('argv: '+(str(type(argv))))


# a recursive fn.
def argv_sys_internal(ii,i,argp):
	if(ii<(i)): print(ii,argp[ii])
	else: return(0x00)
	ii = (ii+(0x01))
	return(0x01+(argv_sys_internal(ii,i,argp)))


# a wrapper fn. (to initialise parameters)
def argv_sys(i,argp):
	if(not i): return(0x00)
	ii = (0x00)
	r = argv_sys_internal(ii,i,argp)
	if(__name__==('__main__')):
		print('Total. '+(str(r)))
		return(0x01)
	return(r)


if(__name__==('__main__')): r = argv_sys(argc,argv)
