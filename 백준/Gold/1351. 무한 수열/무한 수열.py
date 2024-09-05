from collections import defaultdict
import sys
input = sys.stdin.readline

def u(n):
    if t[n] != 0:
        return t[n]
    t[n] = u(n//p)+u(n//q)
    return t[n]

n, p, q = map(int, input().split())
t = defaultdict(int)
t[0] = 1
print(u(n))