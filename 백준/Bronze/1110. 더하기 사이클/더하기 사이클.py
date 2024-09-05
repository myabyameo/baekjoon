import sys
def new(a):
    return a[-1]+str(sum(list(map(int, a)))%10)
n=sys.stdin.readline().strip()
k=new(list(n))
l=1
while True:
    if int(n)==int(k):
        print(l)
        break
    k=new(list(k))
    l+=1