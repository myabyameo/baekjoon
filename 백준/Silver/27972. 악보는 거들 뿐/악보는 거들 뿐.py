n,*li=map(int,open(0).read().split())
t=[1]*n
t2=[1]*n
for i in range(1,n):
    if li[i]>li[i-1]:
        t[i]+=t[i-1]
    if li[i]<li[i-1]:
        t2[i]+=t2[i-1]
    if li[i]==li[i-1]:
        t[i]=t[i-1]
        t2[i]=t2[i-1]
print(max(max(t),max(t2)))