n=int(input())
li=list(map(int,input().split()))
t=list(map(int,input().split()))
ans=0
for i in range(n):
    ans+=(li[i]+li[i+1])*t[i]/2
print(ans)