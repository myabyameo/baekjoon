n=int(input())
li=list(map(int,input().split()))
s=[li[0]]*n
for i in range(1,n):
    s[i]=s[i-1]+li[i]
su=sum(li)
print(sum(li[i]*(su-s[i]) for i in range(n-1)))