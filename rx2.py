import re


s = "Cooool, Python"

ss = [r'Co?',r'Co*',r'Co.',r'Co+',r'^Co',r'n$','Co{3}',]
print(s)
for v in ss:
	mo = re.match(v,s)
	if mo: print(v,mo,type(mo))


s = "Hello, Python!"

ss = [r'H?',r'H*',r'H.',r'H+',]
print(s)
for v in ss:
	mo = re.match(v,s)
	if mo: print(v,mo,type(mo))
