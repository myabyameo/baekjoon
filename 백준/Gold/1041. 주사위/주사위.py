n=int(input())
a,b,c,d,e,f=map(int,input().split())
if n==1:
    print(sum(sorted([a,b,c,d,e,f])[:-1]))
else:
    a,b,c=sorted([min(a,f),min(e,b),min(c,d)])
    print(a*(4*(n-2)*(n-1)+(n-2)**2)+(a+b)*(4*(n-1)+4*(n-2))+(a+b+c)*4)