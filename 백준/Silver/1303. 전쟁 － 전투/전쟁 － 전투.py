import sys
from collections import deque
a,b=map(int,sys.stdin.readline().split())
li=[list(sys.stdin.readline()) for _ in range(b)]
visit=[[True for _ in range(a)] for _ in range(b)]
dic={'B':0,'W':0}
dx=[1,-1,0,0]
dy=[0,0,1,-1]
for i in range(b):
    for j in range(a):
        if visit[i][j]:
            visit[i][j]=False
            num=1
            deq=deque()
            deq.append((i,j))
            string=li[i][j]
            while deq:
                c,k=deq.popleft()
                for m in range(4):
                    x=c+dx[m]
                    y=k+dy[m]
                    if 0<=x<b and 0<=y<a and visit[x][y] and li[x][y]==string:
                        visit[x][y]=False
                        num+=1
                        deq.append((x,y))
            dic[string]+=num**2
print(dic['W'],dic['B'])