a,b=map(int,input().split())
check=[0]*b
li=[0]*a
for i in range(a):
    li[i]=list(map(int,input().split()))[1:]
    for j in li[i]:
        check[j-1]+=1
ans=0
for i in li:
    t=check.copy()
    for j in i:
        t[j-1]-=1
    if 0 not in set(t):
        ans=1
        break
print(ans)