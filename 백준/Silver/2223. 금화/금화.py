a,b,c=map(int,input().split())
if c==0:print(a*b);exit()
m=float('inf')
for i in range(c):
    n,k=map(int,input().split())
    m=min(m,(n-1)//k)
if m==0:print(0)
elif a>m:
    print(m*b+(a-m)//2*b)
else:print(a*b)