import sys
n=int(sys.stdin.readline())
li=list(map(int,sys.stdin.readline().split()))
if n==2 and li[0]==li[1]:
    print(li[-1])
elif n<=2:
    print('A')
else:
    try:
        a=(li[1]-li[2])/(li[0]-li[1])
    except:
        a=1.0
    b=li[1]-li[0]*a
    a=int(a)
    b=int(b)
    possible=True
    for i in range(n-1):
        if li[i]*a+b!=li[i+1]:
            possible=False
            break
    if possible:
        print(int(li[-1]*a+b))
    else:
        print('B')