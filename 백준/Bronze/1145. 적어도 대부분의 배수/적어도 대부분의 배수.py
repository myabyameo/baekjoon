import sys
k=1
a,b,c,d,e=map(int,sys.stdin.readline().split())
while True:
    t=0
    if k%a==0:
        t+=1
    if k%b==0:
        t+=1
    if k%c==0:
        t+=1
    if k%d==0:
        t+=1
    if k%e==0:
        t+=1
    if t>=3:
        print(k)
        break
    k+=1