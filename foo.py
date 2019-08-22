def sum2(a, b):
	print locals()
	return a+b

def sum1(*arg):
	print locals()
	ans = 0
	for ele in arg:
		ans = ans + ele
	return ans

# @todo complete sum3 and sum4
def sum3(**kwargs):
	return "kwargs"

def sum4(*args, **kwargs):
	return "kwargs"


# @todo do the same for min indexes
def max_min_index():
	s=[1,70,80,20,70,80,80,70,80]
	len=len(s)
	max=0
	max_index1=[]
	for i in range(0,len):
		ele=s[i]
		if ele>max:
			max=ele
			max_index1 = [i]
		elif ele==max:
			max_index1.append(i)


print("Maximum value is:",max. len(max_index1))
print("maximum value repeats:" ,max_index1)


Array = map(int, raw_input("Values :").split(" "))
print sum1(*Array)