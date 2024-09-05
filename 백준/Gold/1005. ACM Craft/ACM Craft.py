import sys
from collections import deque
for _ in range(int(sys.stdin.readline())):
    a,b=map(int,sys.stdin.readline().split())
    li=[0]+list(map(int,sys.stdin.readline().split()))
    t=[[] for _ in range(a+1)]
    visit=[0 for _ in range(a+1)]
    dp=[0 for _ in range(a+1)]
    for i in range(b):
        n,m=map(int,input().split())
        t[n].append(m)
        visit[m]+=1
    deq=deque()
    for i in range(1,a+1):
        if visit[i]==0:
            deq.append(i)
            dp[i]=li[i]
    while deq:
        c=deq.popleft()
        for i in t[c]:
            visit[i]-=1
            dp[i]=max(dp[c]+li[i],dp[i])
            if visit[i]==0:
                deq.append(i)
    print(dp[int(sys.stdin.readline())])