def gcd(a,b):
    if a%b:return gcd(b,a%b)
    return b
a,b=map(int,input().split())
li=sorted(list(map(int,input().split())))
t=[]
t=li.copy()
for i in range(1,a):
    t[i]=(t[i-1]*t[i])//gcd(t[i-1],t[i])
d=t[-1]
li2=list(map(int,input().split()))
for i in range(1,b):
    li2[i]=gcd(li2[i-1],li2[i])
m=li2[-1]
yaksu=[]
for i in range(1,int(m**0.5)+1):
    if m%i==0:
        if i*i==m:
            yaksu.append(i)
        else:
            yaksu.extend([i,m//i])
print(len(list(filter(lambda x:x%d==0,yaksu))))