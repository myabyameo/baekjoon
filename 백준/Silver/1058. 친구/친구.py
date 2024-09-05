import sys
from collections import deque
n=int(sys.stdin.readline())
li=[0]*n
dic={x:set() for x in range(n)}
for i in range(n):
    li[i]=list(sys.stdin.readline().strip())
    for j in range(n):
        if li[i][j]=='Y':
            dic[i].add(j)
            dic[j].add(i)
ans=0
for i in range(n):
    check=[True]*n
    check[i]=False
    k=0
    deq=deque()
    for j in dic[i]:
        k+=1
        check[j]=False
        deq.append(j)
    for j in deq:
        for l in dic[j]:
            if check[l]:
                k+=1
                check[l]=False
    ans=max(ans,k)
print(ans)