import sys
input=sys.stdin.readline
n=int(input())
li=list(map(int,input().split()))
t=list(map(int,input().split()))
ans=[0]*n
for j in range(n):
    i=li[j]
    low=j+1
    high=n-1
    while low<=high:
        mid=(low+high)//2
        if t[mid]<=i:
            low=mid+1
        else:
            high=mid-1
    ans[j]=high-j
print(*ans)