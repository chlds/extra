import re


s = 'Hello, Python!'
print(s)

ss = 'Py'
print('find:',ss,end=', ')
r = s.find(ss)
if r == -1: print('Not found')
else: print('index:',r)

# with regular expression

ss = r'^He'
mo = re.search(ss,s)
if mo: print(mo,type(mo))
