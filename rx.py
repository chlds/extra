import re


s = "Cooool, Python!"


ss = r"Co?"
mo = re.match(ss,s)
if mo: print(mo,type(mo))

ss = r"Co*"
mo = re.match(ss,s)
if mo: print(mo,type(mo))

ss = r"Co+"
mo = re.match(ss,s)
if mo: print(mo,type(mo))

# compile

sso = re.compile(ss)
mo = sso.match(s)
if mo: print(mo,type(mo))
