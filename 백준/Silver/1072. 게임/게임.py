import sys
g,w=map(int,sys.stdin.readline().split())
low=0
high=g
wpct=(w*100)//g
if wpct>=99:
    print(-1)
else:
    while low<=high:
        mid=(low+high)//2
        if ((w+mid)*100)//(g+mid)>wpct:
            high=mid-1
            res=mid
        else:
            low=mid+1
    print(res)