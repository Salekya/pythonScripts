#s=[1,2,1,2,3,3,3,4]
#fs=[]
#fs1=[]
#for var in s:
    #ele=s[var]
    #if var not in fs:
        #fs.append(var)
    #else:
        #fs1.append(var)
#print(fs)
#print("Integers appear most no of times:",list(set(fs1)))




def duplicates(s):
    fs=[]
    fs1=[]
    for var in s:
        if var not in fs:
            fs.append(var)
        else:
            fs1.append(var)
    return fs1, fs

fs1, fs=duplicates([1,2,1,2, 3, 3,3, 3, 3, 3, 3, 3,4])
print(fs)
print(fs1)

