import sys
def hae(a,b,c,d):
    for i in range(1,abs(d)+1):
        if d%i:
            continue
        if a*i**3+b*i**2+c*i+d==0:
            return i
        if -a*i**3+b*i**2-c*i+d==0:
            return -i
    return 0
for _ in range(int(sys.stdin.readline())):
    q,w,e,r=map(int,sys.stdin.readline().split())
    ans=set()
    x1=hae(q,w,e,r)
    ans.add(x1)
    a,b,c=q,q*x1+w,q*x1**2+w*x1+e
    d=b**2-4*a*c
    if d==0:
        ans.add(-b/(2*a))
    elif d>0:
        ans.add((-b+(d)**(1/2))/(2*a))
        ans.add((-b-(d)**(1/2))/(2*a))
    ans=list(ans)
    ans.sort()
    if len(ans)==1:
        print('%.4f'%ans[0])
    elif len(ans)==2:
        print('%.4f %.4f' %(ans[0],ans[1]))
    else:
        print('%.4f %.4f %.4f' %(ans[0],ans[1],ans[2]))