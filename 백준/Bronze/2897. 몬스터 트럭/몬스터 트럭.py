a,b=map(int,input().split())
li=[0]*a
for i in range(a):
    li[i]=list(input())
ans=[0,0,0,0,0]
for i in range(a-1):
    for j in range(b-1):
        if '#' not in [li[i][j],li[i+1][j],li[i][j+1],li[i+1][j+1]]:
            ans[[li[i][j],li[i+1][j],li[i][j+1],li[i+1][j+1]].count('X')]+=1
for i in ans:
    print(i)