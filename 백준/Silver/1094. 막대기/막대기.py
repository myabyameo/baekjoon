import sys
n=int(sys.stdin.readline())
li = [2**x for x in range(6,-1,-1)]
k=0
for i in li:
    if n-i>=0:
        n-=i
        k+=1
print(k)