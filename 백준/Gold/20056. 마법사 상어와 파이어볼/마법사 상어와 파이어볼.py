import sys
input=sys.stdin.readline
a,b,c=map(int,input().split())
li=[0]*b
dx=[-1,-1,0,1,1,1,0,-1]
dy=[0,1,1,1,0,-1,-1,-1]
for i in range(b):
    li[i]=list(map(int,input().split()))
    li[i][0]-=1
    li[i][1]-=1
for _ in range(c):
    for i in range(len(li)):
        li[i][0]=(li[i][0]+dx[li[i][-1]]*li[i][-2])%a
        li[i][1]=(li[i][1]+dy[li[i][-1]]*li[i][-2])%a
    field=[[[0,0,0,0,0,0,[]] for _ in range(a)] for _ in range(a)]
    for i in li:
        if field[i[0]][i[1]]==[0,0,0,0,0,0,[]]:
            field[i[0]][i[1]]=i+[1,[i[4]]]
        else:
            field[i[0]][i[1]][2]+=i[2]
            field[i[0]][i[1]][3]+=i[3]
            field[i[0]][i[1]][-2]+=1
            field[i[0]][i[1]][-1].append(i[4])
    li2=[]
    '''for i in field:
        print(*i)'''
    for i in field:
        for j in i:
            if j[-2]==1:
                li2.append(j[:-2])
            else:
                if j[2]<=4 or j[-2]==0:continue
                for k in range(4):
                    lili=j[-1]
                    if all(m%2==0 for m in lili) or all(m%2==1 for m in lili):
                        li2.append([j[0],j[1],j[2]//5,j[3]//j[-2],k*2])
                    else:
                        li2.append([j[0],j[1],j[2]//5,j[3]//j[-2],k*2+1])
    li=li2
    '''print(li)
    print()'''
print(sum(i[2] for i in li))