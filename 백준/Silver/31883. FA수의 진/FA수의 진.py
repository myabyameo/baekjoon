n=int(input())
li=[0]*n
for i in range(n):
    li[i]=list(map(int,input().split()))
ans=0
for i in range(n):
    if ans%(li[i][2]+li[i][3])<li[i][2]:
        ans+=li[i][0]
    else:
        ans+=min(li[i][1],li[i][2]+li[i][3]-ans%(li[i][2]+li[i][3])+li[i][0])
print(ans)