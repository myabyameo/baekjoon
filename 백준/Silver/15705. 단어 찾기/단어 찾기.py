def check(x,y):
    global l,s
    ans=False
    for i in range(8):
        ans=ans or all(0<=x+dx[i]*j<a and 0<=y+dy[i]*j<b and li[x+dx[i]*j][y+dy[i]*j]==s[j] for j in range(l))
    return ans
s=input()
l=len(s)
a,b=map(int,input().split())
li=[0]*a
for i in range(a):
    li[i]=list(input())
dx=[-1,-1,-1,0,0,1,1,1]
dy=[-1,0,1,-1,1,-1,0,1]
real=True
for i in range(a):
    for j in range(b):
        if li[i][j]==s[0]:
            if check(i,j):
                real=False
                print(1)
                break
    if not real:break
if real:print(0)