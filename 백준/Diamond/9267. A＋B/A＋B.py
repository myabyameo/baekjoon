def gcd(o,p):
    while p!=0:
        li.append(o//p)
        o,p=p,o%p
    return o
def gcd2(o,p):
    while p!=0:
        o,p=p,o%p
    return o
li=[]
a,b,c=map(int,input().split())
if a<b:
    d=a
    a=b
    b=d
if b==0:
    if a==0:
        if c==0:
            print('YES')
        else:
            print('NO')
    else:
        if c%a==0:
            print('YES')
        else:
            print('NO')
elif c==a or c==b:
    print('YES')
elif b==1:
    c-=a
    if c>=0:
        print('YES')
    else:
        print('NO')
elif c<b:
    print('NO')
else:
    if c%(g:=gcd2(a,b))==0:
        a//=g;b//=g;c//=g
        gcd(a,b)
        x=1;y=0
        for i in li[::-1]:
            x2=y
            y2=x-y*i
            x=x2;y=y2
        x*=c;y*=c
        m=x//b
        x-=m*b
        y+=m*a
        real=True
        while y>0:
            if x>0 and gcd2(x,y)==1 and a*x+b*y==c:
                print('YES')
                real=False
                break
            x+=b;y-=a
        if real:
            print('NO')
    else:
        print('NO')