from collections import deque
from itertools import combinations
a,b=map(int,input().split())
l=len(str(a))
deq=deque()
deq.append((a,0))
visit=set()
visit.add((a,0))
ans=-1
while deq:
    c,k=deq.popleft()
    if k==b:
        ans=max(ans,c)
        continue
    c=list(str(c))
    for i,j in combinations(range(l),2):
        if i==0 and c[j]=='0':
            continue
        c[i],c[j]=c[j],c[i]
        if (int(''.join(c)),k+1) not in visit:
            deq.append((int(''.join(c)),k+1))
            visit.add((int(''.join(c)),k+1))
        c[i],c[j]=c[j],c[i]
print(ans)