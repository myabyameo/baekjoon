import sys
a=(int(sys.stdin.readline())//100)*100
b=int(sys.stdin.readline())
for i in range(100):
    if a%b==0:
        a=str(a)
        print(a[-2:])
        break
    a+=1