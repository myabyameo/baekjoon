n=int(input())
li=list(map(int,input().split()))
ans=[0]*n
for i in range(n-1,-1,-1):
    if i+li[i]<n-1:
        ans[i]=ans[i+li[i]+1]+1
    else:
        ind=i
        k=0
        while ind<=n-1:
            k+=1
            ind+=1+li[ind]
        ans[i]=k
print(*ans)