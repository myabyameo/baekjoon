from itertools import combinations
def area(li):
    return abs(li[0][0]*li[1][1]+li[1][0]*li[2][1]+li[2][0]*li[0][1]-li[0][1]*li[1][0]-li[1][1]*li[2][0]-li[2][1]*li[0][0])
def check(li):
    return (li[0][0]-li[1][0])*(li[1][0]-li[2][0])*(li[2][0]-li[0][0])==0 and (li[0][1]-li[1][1])*(li[1][1]-li[2][1])*(li[2][1]-li[0][1])==0
n=int(input())
li=[0]*n
for i in range(n):
    li[i]=list(map(int,input().split()))
print(max(area(i) if check(i) else 0 for i in combinations(li,3)))