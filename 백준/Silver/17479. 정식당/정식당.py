a,b,c=map(int,input().split())
normal={}
special={}
service=set()
for _ in range(a):
    n,m=input().split()
    normal[n]=int(m)
for _ in range(b):
    n,m=input().split()
    special[n]=int(m)
for _ in range(c):
    service.add(input())
n=int(input())
li=[0]*n
for i in range(n):
    li[i]=input()
price=0
for i in li:
    if i in normal:
        price+=normal[i]
real=True
for i in li:
    if i in special:
        if price>=20000:
            price+=special[i]
        elif real:
            real=False
            print('No')
if real:
    num=0
    for i in li:
        if i in service:
            if price>=50000 and num==0:
                num+=1
            elif real:
                real=False
                print('No')
if real:print('Okay')