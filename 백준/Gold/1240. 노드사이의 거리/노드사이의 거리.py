import sys
from collections import deque
a,b=map(int,sys.stdin.readline().split())
dic={x+1:[] for x in range(a)}
for i in range(a-1):
    m,n,k=map(int,sys.stdin.readline().split())
    dic[m].append((n,k))
    dic[n].append((m,k))
for _ in range(b):
    x,y=map(int,sys.stdin.readline().split())
    deq=deque()
    deq.append((x,0))
    visit=[True]*(a+1)
    visit[x]=False
    while deq:
        c,k=deq.popleft()
        if c==y:
            print(k)
            break
        for i,j in dic[c]:
            if visit[i]:
                deq.append((i,k+j))
                visit[i]=False