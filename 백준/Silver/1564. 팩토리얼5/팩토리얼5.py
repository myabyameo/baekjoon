n=int(input())
k=1
for i in range(2,n+1):
    k*=i
    k=str(k)
    while k[-1]=='0':
        k=k[:-1]
    k=int(k)
    k%=100000000000000000

print(str(k)[-5:])