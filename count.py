s=[1,2,2,2,2,3]
a=[[x, s.count(x)] for x in set(s)]
#print(a)

s=[1,2,3,4,4,3,3,2]
d={}
for x in s:
    val=d.get(x)
    if val:
        d[x] = val + 1
    else:
        d[x] = 1

print(d)