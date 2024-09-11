import sys
def pow(a,b):
    if b==0:return 1
    if b==1:return a%p
    t=pow(a,b//2)
    if b%2:return (t*t*a)%p
    return (t*t)%p
'''def C(a,b):
    return (fac[a]%p)*pow(fac[b]*fac[a-b]%p,p-2)%p'''
p=10**9+7
a,b,c=map(int,sys.stdin.readline().split())
fac=[1]*((a-1)*b+1)
for i in range(1,(a-1)*b+1):
    fac[i]=fac[i-1]*i%p
li=[0]*(c+2)
minus=[0]*(c+1)
li[0]=[1]*b
li[-1]=[a]*b
for i in range(1,c+1):
    li[i]=list(map(int,sys.stdin.readline().split()))
    t=[0]*b
    for j in range(b):
        t[j]=li[i][j]-li[i-1][j]
    minus[i-1]=t
t=[0]*b
for j in range(b):
    t[j]=li[-1][j]-li[-2][j]
minus[-1]=t
ans=1
for i in minus:
    s=sum(i)
    t=fac[s]
    tmp=1
    for j in i:
        tmp*=fac[j]
        tmp%=p
    t*=pow(tmp,p-2)
    ans*=t%p
    ans%=p
print(ans)