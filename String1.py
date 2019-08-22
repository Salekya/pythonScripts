s="hello"
n=3
j=len(s)
for i in range(0,j):
    e=s[i:i+n]
    if len(e)==n:
        print(e)
