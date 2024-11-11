from collections import deque
def bfs(a,b,field):
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    area=1
    perimeter=4-sum(1 for i in range(4) if 0<=a+dx[i]<n and 0<=b+dy[i]<n and li[a+dx[i]][b+dy[i]]=='#')
    deq=deque()
    deq.append((a,b))
    while deq:
        x,y=deq.popleft()
        for i in range(4):
            s=x+dx[i]
            t=y+dy[i]
            if 0<=s<n and 0<=t<n and field[s][t]==False and li[s][t]=='#':
                field[s][t]=True
                area+=1
                perimeter+=4-sum(1 for i in range(4) if 0<=s+dx[i]<n and 0<=t+dy[i]<n and li[s+dx[i]][t+dy[i]]=='#')
                deq.append((s,t))
    return area,perimeter,field
n=int(input())
li=[0]*n
check=[[False for _ in range(n)] for _ in range(n)]
icecream=deque()
for i in range(n):
    li[i]=list(input())
    for j in range(n):
        if li[i][j]=='#':
            icecream.append((i,j))
ans=0
res=0
for x,y in list(icecream):
    if check[x][y]:
        continue
    check[x][y]=True
    area,perimeter,check=bfs(x,y,check)
    if area>res:
        ans=perimeter
        res=area
    elif area==res:
        ans=min(perimeter,ans)
print(res,ans)