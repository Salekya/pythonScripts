from itertools import combinations
def subset(arr,r):
      return [''.join(x) for x in list(combinations(arr,r))]
arr="hello"
r=2

arry=subset(arr,r)
print(arry)


