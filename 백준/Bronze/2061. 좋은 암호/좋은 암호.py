import sys
a,b=map(int,sys.stdin.readline().split())
n=0
for i in range(2,b):
    if a%i==0:
        print('BAD', i)
        n=1
        break
if n==0:
    print('GOOD')