input()
li=list(map(int,input().split()))
n=li[0]
li=sorted(li[1:])
real=True
for i in li:
    if i<n:n+=i
    else:
        real=False
        break
if real:
    print('Yes')
else:print('No')