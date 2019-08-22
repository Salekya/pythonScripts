s="hello"
val=""
for i, x in enumerate(s):
    if i%2==1:
        val+=x.upper()
    else:
        val+=x.lower()
print(val)

#Using List Comprehensive
print(''.join([x.upper() if i%2==1 else x.lower() for i, x in enumerate("hello")]))

