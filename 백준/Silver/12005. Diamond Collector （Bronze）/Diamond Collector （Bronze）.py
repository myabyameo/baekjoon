a,b=map(int,input().split())
li=[0]*a
for i in range(a):
    li[i]=int(input())
li.sort()
ans=0
for i in range(a):
    n=0
    for j in range(i,a):
        if li[j]-li[i]<=b:
            n+=1
    ans=max(ans,n)
print(ans)