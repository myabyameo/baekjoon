def r(k,l,m,n):
    return ((m-k)**2+(n-l)**2)**0.5
a,b,c,d,e,f=map(int, input().split())
length = sorted([r(a,b,c,d), r(a,b,e,f), r(c,d,e,f)])
if a==c!=e or a!=c==e:
    print(2*((length[-1]+length[-2])-(length[0]+length[1])))
elif a==c==e or (d-b)/(c-a) == (f-d)/(e-c):
    print(-1)
else:
    print(2*((length[-1]+length[-2])-(length[0]+length[1])))