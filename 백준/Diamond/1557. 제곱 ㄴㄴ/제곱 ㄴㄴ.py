def sqn(m):
    t=0
    for i in range(1,int(m**0.5)+1,1):
        t+=che[i]*(m//(i*i))
    return t
n=int(input())
p=100001
che=[0]*p
che[1]=1
for i in range(1,p):
    if che[i]!=0:
        for j in range(i*2, p, i):
            che[j]-=che[i]
low=0
high=2000000000
while low<=high:
    mid=(low+high)//2
    if sqn(mid)>=n:
        high=mid-1
    else:
        low=mid+1
print(high+1)