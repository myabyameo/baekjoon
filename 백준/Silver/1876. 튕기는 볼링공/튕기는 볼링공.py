from math import tan,sin,radians
for _ in range(int(input())):
    a,b=map(float,input().split())
    b=radians(b)
    a*=100
    n=0
    while True:
        if -16/sin(b)<=a-(85/tan(b))*n<=16/sin(b):
            print('yes')
            break
        elif a-(85/tan(b))*n>16/sin(b):
            n+=1
        else:
            print('no')
            break