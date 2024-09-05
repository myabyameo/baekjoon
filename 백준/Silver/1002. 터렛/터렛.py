import math
import sys
n = int(sys.stdin.readline())
for _ in range(n):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())
    ww = math.sqrt((x1-x2)**2 + (y1-y2)**2) 
    if ww == 0 and r1 == r2 : 
        print(-1)
    elif abs(r1-r2) == ww or r1 + r2 == ww:  
        print(1)
    elif abs(r1-r2) < ww  and ww < (r1+r2) :
        print(2)
    else:
        print(0)