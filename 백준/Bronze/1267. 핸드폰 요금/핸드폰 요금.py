a=int(input())
li=list(map(int,input().split()))
m=0;y=0
for i in li:
    m+=(i//60+1)*15
    y+=(i//30+1)*10
if m>y:
    print('Y',y)
elif m==y:
    print('Y','M',y)
else:
    print('M',m)