import sys
a, b,n = map(int, sys.stdin.readline().split())
for i in range(n) :
    a = (a%b)*10
    hehe = a//b
 
print(hehe)