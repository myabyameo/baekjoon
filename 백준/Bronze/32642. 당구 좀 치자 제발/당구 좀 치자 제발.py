n=int(input())
a=0
ans=0
for i in map(int,input().split()):
    if i==1:
        a+=1
    else:a-=1
    ans+=a
print(ans)