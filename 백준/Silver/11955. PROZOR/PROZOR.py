import sys
input=sys.stdin.readline
a,b,c=map(int,input().split())
li=[0]*a
for i in range(a):
    li[i]=list(input().strip())
m=0
for i in range(a-c+1):
    for j in range(b-c+1):
        num=0
        for k in range(1,c-1):
            for l in range(1,c-1):
                if li[i+k][j+l]=='*':
                    num+=1
        if num>m:
            m=num
            ans=i,j
for i in range(c):
    if i==0 or i==c-1:
        li[ans[0]][ans[1]+i]='+'
        for j in range(c):
            if j==0 or j==c-1:
                li[ans[0]+j][ans[1]+i]='+'
            else:
                li[ans[0]+j][ans[1]+i]='|'
    else:
        li[ans[0]][ans[1]+i]='-'
        li[ans[0]+c-1][ans[1]+i]='-'
print(m)
for i in li:
    print(''.join(i))