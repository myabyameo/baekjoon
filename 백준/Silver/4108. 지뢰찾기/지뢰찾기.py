while True:
    a,b=map(int,input().split())
    if a*b==0:break
    li=[0]*a
    for i in range(a):
        li[i]=list(input())
    dx=[1,1,1,0,0,-1,-1,-1]
    dy=[1,0,-1,1,-1,1,0,-1]
    for i in range(a):
        for j in range(b):
            if li[i][j]=='.':
                ans=0
                for k in range(8):
                    if 0<=i+dx[k]<a and 0<=j+dy[k]<b and li[i+dx[k]][j+dy[k]]=='*':
                        ans+=1
                li[i][j]=str(ans)
    li=list(map(lambda x:''.join(x),li))
    for i in li:
        print(i)