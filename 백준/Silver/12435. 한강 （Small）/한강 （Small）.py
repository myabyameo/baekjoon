import sys
n=1000001
che=[0]*n
che2=[x for x in range(n)]
for i in range(2,n):
    for j in range(i+i,n,i):
        che[j]+=1
    if che2[i]==i:
        che2[i]-=i
        for j in range(i+i,n,i):
            if che2[j]==j:che2[j]=i
for _ in range(int(sys.stdin.readline())):
    a,b=map(int,sys.stdin.readline().split())
    t=0
    for i in range(2,a):
        if che[a]==che[i] and che2[i]>=b:
            t+=1
    print(f'Case #{_+1}: {t}')