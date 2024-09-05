import sys
for _ in range(int(sys.stdin.readline())):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    d1=[] ; d2=[]
    for i in range(int(sys.stdin.readline())):
        x,y,r=map(int,sys.stdin.readline().split())
        if int(((x-x1)**2+(y-y1)**2)**0.5) < r:
            d1.append((x,y,r))
        if int(((x-x2)**2+(y-y2)**2)**0.5) < r:
            d2.append((x,y,r))
    d1=set(d1)
    d2=set(d2)
    print(len(d1|d2)-len(d1&d2))