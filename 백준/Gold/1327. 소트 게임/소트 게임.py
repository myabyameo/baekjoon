from collections import deque
deq=deque()
a,b=map(int,input().split())
li=list(map(int,input().split()))
se=set()
se.add(''.join(map(str,li)))
so=sorted(li)
deq.append((li,0))
real=True
while deq:
    c,k=deq.popleft()
    if c==so:
        print(k)
        real=False
        break
    for i in range(a-b+1):
        c2=c[:i]+c[i:i+b][::-1]+c[i+b:]
        c2=''.join(map(str,c2))
        if c2 in se:
            continue
        se.add(c2)
        deq.append((list(map(int,list(c2))),k+1))
if real:
    print(-1)