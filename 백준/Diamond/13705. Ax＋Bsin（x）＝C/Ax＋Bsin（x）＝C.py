from decimal import *
getcontext().prec=150
getcontext().rounding=ROUND_HALF_UP
pi=Decimal('3.1415926535897932384626433832795028841971693993751058209749')
def sin(a):
    a%=Decimal(2*pi)
    n=Decimal(1)
    ans=Decimal(a)
    d=ans
    while abs(d)>=10**(-60):
        n+=2
        d=(d*a*a)/(Decimal(n*(n-1))*Decimal(-1))
        ans+=d
    return ans
f=lambda x:a*x+b*sin(x)-c
a,b,c=map(int,input().split())
low=Decimal(0)
high=Decimal(10**6)
mid=(high+low)/Decimal(2)
while abs(high-low)>=10**(-60):
    if f(mid)>0:high=mid
    else:low=mid
    mid=(high+low)/Decimal(2)
print(round(mid,6))