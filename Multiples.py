#s=("enter the numbers")
def multiple(var):
    #var=range(1,101)
    ans = []
    for j in range(1, var):
        tmp = ""

        if j%3==0:
            tmp = tmp + 'Fizz'


        if j%5==0:
            tmp += "Buzz"

        ans.append(tmp or j)

    return ans

ans = multiple(50)
print(ans)






