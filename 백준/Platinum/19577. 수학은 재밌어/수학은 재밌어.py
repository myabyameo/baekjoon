n=10**6+1
che=[i for i in range(n)]
for i in range(2,n):
    if che[i]==i:
        for j in range(i,n,i):
            che[j]=che[j]-che[j]//i
n=int(input())
if n>2:
    li=[]
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            li.append(i)
            li.append(n//i)
    li.sort()
    real=True
    for i in li:
        if i<=10**6 and i*che[i]==n:
            print(i)
            real=False
            break
    if real:print(-1)
else:
    print(n)