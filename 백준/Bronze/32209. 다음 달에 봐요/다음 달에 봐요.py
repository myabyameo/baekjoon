k=0
for i in range(int(input())):
    a,b=input().split()
    if a=='1':
        k+=int(b)
    elif a=='2':
        k-=int(b)
    if k<0:
        break
if k>=0:print('See you next month')
else:print('Adios')