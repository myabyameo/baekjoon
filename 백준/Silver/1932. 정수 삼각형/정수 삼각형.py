import sys
input=sys.stdin.readline
n=int(input())
li=[0]*n
for i in range(n):
    li[i]=list(map(int,input().split()))
for i in range(1,n):
    li[i][0]+=li[i-1][0]
    li[i][-1]+=li[i-1][-1]
for i in range(2,n):
    for j in range(1,i):
        li[i][j]+=max(li[i-1][j],li[i-1][j-1])
print(max(li[-1]))