li=[[0 for _ in range(101)] for _ in range(101)]
a,b=map(int,input().split())
for _ in range(a):
    x,y,n,m=map(int,input().split())
    for i in range(x,n+1):
        for j in range(y,m+1):
            li[i][j]+=1
ans=0
for i in li:
    for j in i:
        if j>b:ans+=1
print(ans)