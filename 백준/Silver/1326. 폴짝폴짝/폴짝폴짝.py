from collections import deque
a=int(input())
li=list(map(int,input().split()))
check={x:float('inf') for x in range(a)}
m,n=map(int,input().split())
check[m-1]=0
deq=deque()
deq.append((m-1,0))
real=True
while deq:
    c,k=deq.popleft()
    if c==n-1:
        print(k)
        real=False
        break
    for i in range(c,a,li[c]):
        if check[i]>k+1:
            check[i]=k+1
            deq.append((i,k+1))
    for i in range(c,-1,-li[c]):
        if check[i]>k+1:
            check[i]=k+1
            deq.append((i,k+1))
if real:
    print(-1)