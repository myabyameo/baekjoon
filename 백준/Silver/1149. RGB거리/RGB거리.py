import sys
a=int(sys.stdin.readline())
li=[0]*a
for i in range(a):
    li[i]=list(map(int,sys.stdin.readline().split()))
t=[[1,2],[0,2],[0,1]]
for i in range(1,a):
    for j in range(3):
        li[i][j]=min(li[i-1][t[j][0]]+li[i][j], li[i-1][t[j][1]]+li[i][j])
print(min(li[-1]))