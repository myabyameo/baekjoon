import sys
from collections import deque
a,b=map(int,sys.stdin.readline().split())
t=deque([x+1 for x in range(a)])
li = deque(map(int,sys.stdin.readline().split()))
l=0
for i in list(li):
    ind=t.index(i)
    m=min(ind, a-ind)
    l+=m
    if m==ind:
        t.rotate(-m)
    elif m==a-ind:
        t.rotate(m)
    t.popleft()
    a-=1
print(l)