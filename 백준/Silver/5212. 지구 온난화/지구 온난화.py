a,b=map(int,input().split())
li=[0]*a
for i in range(a):
    li[i]=list('.'+input()+'.')
li.insert(0,['.']*(b+2))
li.append(['.']*(b+2))
dx=[1,-1,0,0]
dy=[0,0,1,-1]
ans=[i.copy() for i in li]
width=[b+1,0]
height=[a+1,0]
for i in range(1,a+1):
    for j in range(1,b+1):
        if li[i][j]=='.':continue
        res=0
        for k in range(4):
            x=i+dx[k]
            y=j+dy[k]
            if li[x][y]=='.':res+=1
        if res>=3:
            ans[i][j]='.'
        else:
            width[0]=min(width[0],j)
            width[1]=max(width[1],j)
            height[0]=min(height[0],i)
            height[1]=max(height[1],i)
ans=ans[height[0]:height[1]+1]
ans=list(map(lambda x:x[width[0]:width[1]+1],ans))
ans=list(map(lambda x:''.join(x),ans))
for i in ans:print(i)