import sys
for _ in range(int(sys.stdin.readline())):
    a,b=map(int,sys.stdin.readline().split())
    l=b-a
    k=int(l**0.5)
    t=l-k**2
    times=(k-1)*2+1
    if t==0:
        print(times)
    elif t%k==0:
        print(times+t//k)
    else:
        print(times+t//k+1)