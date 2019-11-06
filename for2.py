s = 'Hello, Python!'

g = (i for i in s.split())
print(g,type(g))
for i in g: print(i,type(i))

l = [i for i in s.split()]
print(l,type(l))
for i in l: print(i,type(i))
