import sys
n=int(sys.stdin.readline())
A=sorted(list(map(int,sys.stdin.readline().split())))
B=sorted(list(map(int,sys.stdin.readline().split())))
B=B[::-1]
m=0
for i in range(n):
    m+=A[i]*B[i]
print(m)