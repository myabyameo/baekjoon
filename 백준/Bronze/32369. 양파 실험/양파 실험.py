li=[1,1]
a,b,c=map(int,input().split())
for i in range(a):
    li[0]+=b
    li[1]+=c
    if li[0]==li[1]:
        li[1]-=1
    elif li[0]<li[1]:
        li.reverse()
print(*li)