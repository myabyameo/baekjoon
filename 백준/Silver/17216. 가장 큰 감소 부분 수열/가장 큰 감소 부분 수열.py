n=int(input())
li=list(map(int,input().split()))
dp=li.copy()
for i in range(1,n):
    for j in range(i):
        if li[i]<li[j]:
            dp[i]=max(dp[i],dp[j]+li[i])
print(max(dp))