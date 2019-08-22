s="hello"
j=len(s)
n=2
for i in range(j):
    for e in range(0,i+1):
        print(s[i:e])
    n=n+1