import sys
n=int(sys.stdin.readline())
if n//10<10:
    print(n)
else:
    k=0
    for i in range(100,n+1):
        a=str(i)
        if int(a[0])+int(a[2])==2*int(a[1]):
            k+=1
    print(k+99)