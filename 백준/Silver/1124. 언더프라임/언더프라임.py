import sys
def soinsubunhae(x):
    num = 0
    for i in range(2,int(x**0.5)+1):
        while x%i==0:
            num+=1
            x=x//i
    if x!=1:
        num+=1
    return num
n=50
che=[True]*n
che[1]=False
for i in range(2,n):
    if che[i]==True:
        for j in range(i+i, n, i):
            che[j]=False
a,b=map(int,sys.stdin.readline().split())
k=0
for i in range(a,b+1):
    if che[soinsubunhae(i)]:
        k+=1
print(k)