from math import floor

def check(d):
    if all(floor(b+d*(i+1))==li[i] for i in range(a)):
        return True
    return False
a,b=map(int,input().split())
if a==0:
    print(0.0)
else:
    li=list(map(int,input().split()))
    ans=float('inf')
    for i,j in list(enumerate(li))[::-1]:
        d=(j-b)/(i+1)
        if 0<=d<ans and check(d):
            ans=d
    print(ans if ans!=float('inf') else -1)