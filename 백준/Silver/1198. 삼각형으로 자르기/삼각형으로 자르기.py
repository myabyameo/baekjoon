from itertools import combinations
def S(x1,y1,x2,y2,x3,y3):
    return abs(x2*y1+x3*y2+x1*y3-x1*y2-x2*y3-x3*y1)/2
n=int(input())
li=[0]*n
for i in range(n):
    li[i]=list(map(int,input().split()))
li=li+li+li
m=0
for i,j,k in combinations(li,3):
    m=max(m,S(i[0],i[1],j[0],j[1],k[0],k[1]))
print(m)