li=[0]*1001
for i in range(int(input())):
    a,b=map(int,input().split())
    li[a]=b
m=0
l=1
ans=0
M=max(li)
ind=0
for i in li:
    if i>m:
        ans+=l*m
        m=i
        l=1
    else:l+=1
    if i==M:break
    ind+=1
ind2=1001
m=0
l=1
for i in li[::-1]:
    if i>m:
        ans+=l*m
        m=i
        l=1
    else:l+=1
    if i==M:break
    ind2-=1
print(ans+(ind2-ind)*M)