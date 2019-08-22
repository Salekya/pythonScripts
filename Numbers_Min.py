a=[1,-2,4,50,-1,-1,-2,-2]
l=len(a)
m=a[0]
m_index=[]
for j in range(0,l):
    ele=a[j]
    if ele<m:
        m=ele
        m_index=[j]
    elif ele==m:
        m_index.append(j)
print(m,m_index)