a,b=map(int,input().split())
li=[0]*a
for i in range(a):
    li[i]=list(map(int,input().split()))
n=int(input())
ans=0
for i in range(1,a-1):
    for j in range(1,b-1):
        if sorted([li[i-1][j-1],li[i-1][j],li[i-1][j+1],li[i][j-1],li[i][j],li[i][j+1],li[i+1][j-1],li[i+1][j],li[i+1][j+1]])[4]>=n:ans+=1
print(ans)