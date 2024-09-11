def mul(a,b):
    ans=[[0 for _ in range(55)] for _ in range(55)]
    for i in range(55):
        for j in range(55):
            for k in range(55):
                ans[i][j]+=a[i][k]*b[k][j]%p
            ans[i][j]%=p
    return ans
def pow(a,b):
    if b==1:return a
    t=pow(a,b//2)
    if b%2:return mul(mul(t,t),a)
    return mul(t,t)
k,n=map(int,input().split())
p=10**9+7
li=[list(map(int,list(('1'*i).ljust(55,'0')))) for i in range(1,56)]
print(sum(pow(li,n-1)[k+1])%p if n>1 else 1)