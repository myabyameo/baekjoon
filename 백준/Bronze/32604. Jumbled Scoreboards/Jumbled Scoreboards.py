n=int(input())
li=[0]*n
t=[0]*n
for i in range(n):
    a,b=map(int,input().split())
    li[i]=a
    t[i]=b
if li==sorted(li) and t==sorted(t):
    print('yes')
else:print('no')