a,b=map(int,input().split())
li=list(map(int,input().split()))
su=[0]*a
for i in range(1,a):
    su[i]=abs(li[i]-li[i-1])+su[i-1]
for i in range(b):
    n,m=map(int,input().split())
    print(su[m-1]-su[n-1])