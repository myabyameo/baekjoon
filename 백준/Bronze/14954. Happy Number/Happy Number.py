def f(a):
    ans=0
    a=str(a)
    for i in a:
        ans+=int(i)**2
    return ans
n=int(input())
se=set()
real=False
while n not in se:
    se.add(n)
    if n==1:
        real=True
        break
    n=f(n)
if real:print('HAPPY')
else:print('UNHAPPY')