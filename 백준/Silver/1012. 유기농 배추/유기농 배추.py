import sys
from collections import deque
def bfs(t):
    deq=deque()
    deq.append(t)
    while deq:
        x,y=deq.popleft()
        if not visit[y][x]:
            visit[y][x]=True
            ans.add(ret)
        for i in range(4):
            a1= x + dx[i]
            b1= y + dy[i]
            if a1>=a or a1<0 or b1>=b or b1<0:
                continue
            if visit2[b1][a1]==visit[b1][a1]==False:
                visit[b1][a1]=True
                ans.add(ret)
                deq.append([a1, b1])
for _ in range(int(sys.stdin.readline())):
    a,b,c=map(int,sys.stdin.readline().split())
    t=[list(map(int,sys.stdin.readline().split())) for i in range(c)]
    t.sort()
    visit=[[False]*a for _ in range(b)]
    visit2=[[True]*a for _ in range(b)]
    for i in t:
        visit2[i[1]][i[0]]=False
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    ans=set()
    for ret in range(c):
        bfs(t[ret])
    print(len(ans))