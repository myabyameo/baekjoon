def dist(a,b,c,d):
    return ((a-c)**2+(b-d)**2)**0.5
a,b,c,d=map(int,input().split())
di=dist(a,b,0,0)
ans=di
n=di//c
ans=min(n*d+abs(di-c*n),ans)
ans=min((n+1)*d+abs(di-c*(n+1)),ans)
if n>0:
    ans=min(ans,d*(n+1))
if c>di:
    ans=min(ans,d*2)
print(float(ans))