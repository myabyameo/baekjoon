n=int(input())
li=[0]*n
for i in range(n):
    li[i]=list(map(int,input().split()))
dic={i:set() for i in range(1,n+1)}
for k in range(5):
    for i in range(n):
        for j in range(i+1,n):
            if li[i][k]==li[j][k]:
                dic[i+1].add(j+1)
                dic[j+1].add(i+1)
l=-1
ans=0
for i in dic:
    if len(dic[i])>l:
        l=len(dic[i])
        ans=i
print(ans)