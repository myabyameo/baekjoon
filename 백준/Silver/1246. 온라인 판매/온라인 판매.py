a,b=map(int,input().split())
li=[0]*b
for i in range(b):
    li[i]=int(input())
li.sort()
ans=0
for i in range(b):
    if ans<li[i]*min((b-i),a):
        ans=li[i]*min(b-i,a)
        ans2=li[i]
print(ans2,ans)