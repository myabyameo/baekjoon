n=int(input())
ans=0
for i in range(1,int(n**0.5)+1):
    for j in range(i,n+1):
        if i*j<=n:
            ans+=1
print(ans)