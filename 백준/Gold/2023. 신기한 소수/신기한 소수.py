def back(k,i):
    global ans
    if i==n:
        print(k)
        return 0
    for j in [1,3,7,9]:
        if all((k*10+j)%i for i in range(2,int((k*10+j)**0.5)+1)):
            back(k*10+j,i+1)
li=[2,3,5,7]
n=int(input())
ans=[]
for i in li:
    back(i,1)