def string(s,n):
    j=len(s)

    for i in range(0,j):
        e=s[i:i+n]
        if len(e)==n:
            print(e)
    return e

e=string("hello",3)
print(e)
