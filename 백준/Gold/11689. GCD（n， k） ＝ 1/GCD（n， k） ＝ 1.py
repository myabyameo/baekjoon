n=int(input())
ans=n
li=[]
for i in range(2,int(n**0.5)+1):
    if n%i==0:
        ans-=ans//i
        while n%i==0:
            n//=i
if n>1:
    ans-=ans//n
print(ans)