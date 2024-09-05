import sys
from itertools import combinations
def zmrl(a,b):
    return (a**2+b**2)**0.5
for _ in range(int(sys.stdin.readline())):
    n=int(sys.stdin.readline())
    li=[0]*n
    for _ in range(n):
        li[_]=list(map(int,sys.stdin.readline().split()))
    xsum=0
    ysum=0
    for i in range(n):
        xsum+=li[i][0]
        ysum+=li[i][1]
    ans=float('inf')
    for i in combinations(li,n//2):
        x=0;y=0
        for j in i:
            x+=j[0]
            y+=j[1]
        ans=min(ans,zmrl(xsum-2*x,ysum-2*y))
    print(ans)