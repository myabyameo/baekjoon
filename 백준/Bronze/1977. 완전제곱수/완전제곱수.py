import sys
a=int(sys.stdin.readline())
b=int(sys.stdin.readline())
li=[]
for i in range(a,b+1):
    if i==int(i**0.5)**2:
        li.append(i)
try:
    print(f'{sum(li)}\n{li[0]}')
except:
    print(-1)