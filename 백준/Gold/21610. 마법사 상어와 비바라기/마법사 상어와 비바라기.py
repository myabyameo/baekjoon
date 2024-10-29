import sys
input=sys.stdin.readline
a,b=map(int,input().split())
li=[0]*a
for i in range(a):
    li[i]=list(map(int,input().split()))
t=[0]*b
for i in range(b):
    t[i]=list(map(int,input().split()))
cloud=[[a-2,0],[a-1,0],[a-2,1],[a-1,1]]
dx=[0,0,-1,-1,-1,0,1,1,1]
dy=[0,-1,-1,0,1,1,1,0,-1]
for i in range(b):
    li2=[]
    for x,y in cloud:
        rx=(x+dx[t[i][0]]*t[i][1])%a
        ry=(y+dy[t[i][0]]*t[i][1])%a
        li[rx][ry]+=1
        li2.append((rx,ry))
    for x,y in li2:
        if 0<=x-1<a and 0<=y-1<a and li[x-1][y-1]:
            li[x][y]+=1
        if 0<=x-1<a and 0<=y+1<a and li[x-1][y+1]:
            li[x][y]+=1
        if 0<=x+1<a and 0<=y-1<a and li[x+1][y-1]:
            li[x][y]+=1
        if 0<=x+1<a and 0<=y+1<a and li[x+1][y+1]:
            li[x][y]+=1
    k=[]
    for x in range(a):
        for y in range(a):
            if li[x][y]>=2 and (x,y) not in li2:
                k.append((x,y))
                li[x][y]-=2
    cloud=k
    if i==b-1:
        print(sum(sum(i) for i in li))