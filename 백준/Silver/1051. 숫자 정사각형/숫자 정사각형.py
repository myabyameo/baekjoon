import sys
a, b = map(int, sys.stdin.readline().split())
t=[]
for i in range(a):
    t.append(list(sys.stdin.readline()))
size = min(a, b)
num=0
for k in range(size):
    for i in range(max(a,b)-size+1):
        for j in range(b-size+1):
            try:
                if t[i][j]==t[i][j+size-1]==t[i+size-1][j]==t[i+size-1][j+size-1]:
                    print(size**2)
                    num=size**2
                    break
            except:
                break
        if num != 0:
            break
    if num!=0:
        break
    size-=1