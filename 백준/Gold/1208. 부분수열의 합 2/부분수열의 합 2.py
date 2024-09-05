import sys
from bisect import bisect_left, bisect_right
from itertools import combinations
a,b=map(int,sys.stdin.readline().split())
li=list(map(int,sys.stdin.readline().split()))
n=a//2
li1=li[:n]
s1=[]
for i in range(n):
    for j in combinations(li1,i+1):
        s1.append(sum(j))
s1.sort()
li2=li[n:]
s2=[]
for i in range(a-n):
    for j in combinations(li2,i+1):
        s2.append(sum(j))
s2.sort()
ans=0
for i in s1:
    ans+=bisect_right(s2,b-i)-bisect_left(s2,b-i)
ans+=bisect_right(s1,b)-bisect_left(s1,b)
ans+=bisect_right(s2,b)-bisect_left(s2,b)
print(ans)