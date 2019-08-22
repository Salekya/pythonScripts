def addition(*args, **kwargs):
    print(locals())
    ans=0
    for ele in args:
        ans=ans+ele

    for v in kwargs.values():
        ans = ans + v
    return ans





ans = addition(3, 5, a=1, b=3, c=3, d=6)
print(ans)