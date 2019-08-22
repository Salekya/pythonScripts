#Find Max and Min
s=[-1,-34,-56,-4,-56,-9,-56,-9,-1,-1]
#s = [10, 10 , 10]
length=len(s)
maxi=s[0]
mini=s[0]
maxi_i=[]
mini_i=[]
for var in range(0,length):
    ele=s[var]
    if ele>maxi:
        maxi=ele
        maxi_i=[var]
    elif ele==maxi:
        maxi_i.append(var)

    if ele<mini:
        mini=ele
        mini_i=[var]
    elif ele==mini:
        mini_i.append(var)
print ("Maximum No:" ,maxi,"mimimum number:",mini,"Maximum index",maxi_i,"Minimum index",mini_i)

