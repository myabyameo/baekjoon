import sys
a,b=map(int,sys.stdin.readline().split())
se=set()
for i in range(a):
    se.add(sys.stdin.readline().strip())
for _ in range(b):
    li=input().split(',')
    for i in li:
        if i in se:
            se.remove(i)
            a-=1
    print(a)