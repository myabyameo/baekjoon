import sys
a,b=map(int,sys.stdin.readline().split())
t=0
real=True
while b!=a:
    t+=1
    s=b
    if b%10==1:
        b//=10
    elif b%2==0:
        b//=2
    if b==a:
        real=False
        print(t+1)
        break
    if t==b:break
if real:
    print(-1)