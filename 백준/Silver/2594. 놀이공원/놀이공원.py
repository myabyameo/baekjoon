n=int(input())
ans=0
li=[0]*n
for i in range(n):
    a,b=map(int,input().split())
    a=(a//100)*60+a%100-10
    b=(b//100)*60+b%100+10
    li[i]=(a,b)
li.insert(0,(600,600))
li.append((1320,1320))
li.sort()
now=600
for i,j in li:
    ans=max(ans,i-now)
    now=max(now,j)
print(ans)