from collections import deque
n=int(input())
deq=deque()
li=deque([i+1 for i in range(n)])
for i in map(int,input().split()):
    if i==1:
        t=li.popleft()
    elif i==2:
        k,t=li.popleft(),li.popleft()
        li.appendleft(k)
    else:
        t=li.pop()
    deq.appendleft(t)
print(*map(lambda x:x[0]+1,sorted(list(enumerate(list(deq))),key=lambda x:x[1])))