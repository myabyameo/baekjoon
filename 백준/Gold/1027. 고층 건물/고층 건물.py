import sys
def slope(x1,x2,y1,y2):
    return (y2-y1)/(x2-x1)
n=int(sys.stdin.readline())
li=list(map(int,sys.stdin.readline().split()))
res=0
for i in range(n):
    ans=0
    if i!=0:
        ans+=1
        k=slope(i,i-1,li[i],li[i-1])
        for j in range(i-2,-1,-1):
            m=slope(i,j,li[i],li[j])
            if m<k:
                ans+=1
                k=m
    if i!=n-1:
        ans+=1
        k=slope(i,i+1,li[i],li[i+1])
        for j in range(i+2,n):
            m=slope(i,j,li[i],li[j])
            if m>k:
                ans+=1
                k=m
    res=max(res,ans)
print(res)