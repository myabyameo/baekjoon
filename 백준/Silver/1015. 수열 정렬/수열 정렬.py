import sys
n=int(sys.stdin.readline())
li=list(map(int,sys.stdin.readline().split()))
t=[0]*n
for i in range(n):
    t[i]=[li[i], i]
t.sort(key=lambda x:x[0])
for i in range(n):
    t[i]=[t[i][1], i]
t.sort(key=lambda x:x[0])
for i in range(n):
    t[i]=t[i][1]
print(*t)