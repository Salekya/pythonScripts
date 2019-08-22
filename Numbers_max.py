s=[1,70,80,20,70,80,80,70,80]
len=len(s)
max=0
max_Index=[]
#max_index1=[]
for i in range(0,len):
    ele=s[i]
    if ele>max:
        max=ele
        max_Index= [i]
    elif ele==max:
        max=ele
        max_Index.append(i)
print("Maximum value is:",max)
print("Maximum value index is:", max_Index)
#print("maximum value repeats:" ,max_index1)



