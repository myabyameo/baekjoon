import sys
a,b=map(int, sys.stdin.readline().split())
c,d=map(int, sys.stdin.readline().split())
j = a*d+b*c
m = b*d
li = []
def G(m, M):
    M=M%m
    if M!=0:
        G(M,m)
    else:
        li.append(m)
G(min(j,m), max(j,m))
print(j//li[0], m//li[0])