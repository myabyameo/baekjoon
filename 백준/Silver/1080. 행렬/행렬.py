import sys
input=sys.stdin.readline
a,b=map(int,input().split())
li=[0]*a
t=[0]*a
for i in range(a):
    li[i]=list(input())
for i in range(a):
    t[i]=list(input())
ans=0
for i in range(a-2):
    for j in range(b-2):
        if li[i][j]!=t[i][j]:
            ans+=1
            for x in range(3):
                for y in range(3):
                    if li[i+x][j+y]=='0':
                        li[i+x][j+y]='1'
                    else:
                        li[i+x][j+y]='0'
if li==t:
    print(ans)
else:print(-1)