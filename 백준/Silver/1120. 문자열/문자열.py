import sys
def chai(a,b,l):
    n=0
    for i in range(l):
        if a[i]!=b[i]:
            n+=1
    return n
a, b= sys.stdin.readline().split()
la=len(a)
l=len(b)-la+1
li=[0]*l
for i in range(l):
    li[i]=chai(a,b[i:la+i],la)
print(min(li))