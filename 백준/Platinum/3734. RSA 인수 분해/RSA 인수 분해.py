import math
n,k=map(int,input().split())
nk=n*k
for x in range(-10**5,10**5+1):
    a=x*x+4*nk
    y=math.isqrt(a)
    if y**2!=a:continue
    q=(x+y)//2
    p=(y-q)//k
    if p*q==n and 1<p<=q<n:
        print(f'{int(p)} * {int(q)}')
        break