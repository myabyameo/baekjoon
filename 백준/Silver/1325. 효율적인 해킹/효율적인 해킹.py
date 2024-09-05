from collections import deque
import sys
a,b=map(int,sys.stdin.readline().split())
t=[[] for _ in range(a+1)]
for i in range(b):
    n,m=map(int,sys.stdin.readline().split())
    t[m]+=[n]
ans=dict()
for i in range(a):
    li=[0]*(a+1)
    li[i+1]=1
    deq=deque([i+1])
    while deq:
        c=deq.popleft()
        for j in t[c]:
            if li[j]==0:
                deq.append(j)
                li[j]=1
    ans[i+1]=sum(li)
M=max(ans.values())
an=[]
for i in range(1,a+1):
    if ans[i]==M:
        an.append(i)
print(*an)