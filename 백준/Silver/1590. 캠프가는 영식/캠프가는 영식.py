from bisect import bisect_left
a,b=map(int,input().split())
li=set()
for i in range(a):
    n,m,k=map(int,input().split())
    for j in range(k):
        li.add(n+m*j)
li=sorted(list(li))
try:
    print(li[bisect_left(li,b)]-b)
except:print(-1)