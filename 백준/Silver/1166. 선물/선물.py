import sys
n,l,w,h=map(int,sys.stdin.readline().split())
low=0
high=l
for _ in range(10000):
    mid=(low+high)/2
    if (l//mid)*(w//mid)*(h//mid)<n:
        high=mid
    else:
        low=mid
print('%.10f'%(high))