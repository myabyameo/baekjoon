import sys
from collections import deque
a,b=map(int,sys.stdin.readline().split())
deq = deque([x+1 for x in range(a)])
li=[0]*a
l=b-1
while a>0:
    li[a-1]=deq[l]
    del deq[l]
    l+=b-1
    a-=1
    try:
        l%=a
    except:
        continue
print('<'+f'{li[::-1]}'[1:-1]+'>')