def cross(x,y):
    global ln
    n=0
    k=0
    i=1
    while 0<=x+i<ln and 0<=y+i<ln:
        if li[x+i][y+i]=='.':
            break
        elif li[x+i][y+i]=='W':
            k+=1
            i+=1
        elif li[x+i][y+i]=='B':
            n+=k
            break
    k=0
    i=1
    while 0<=x-i<ln and 0<=y+i<ln:
        if li[x-i][y+i]=='.':
            break
        elif li[x-i][y+i]=='W':
            k+=1
            i+=1
        elif li[x-i][y+i]=='B':
            n+=k
            break
    k=0
    i=1
    while 0<=x+i<ln and 0<=y-i<ln:
        if li[x+i][y-i]=='.':
            break
        elif li[x+i][y-i]=='W':
            k+=1
            i+=1
        elif li[x+i][y-i]=='B':
            n+=k
            break
    k=0
    i=1
    while 0<=x-i<ln and 0<=y-i<ln:
        if li[x-i][y-i]=='.':
            break
        elif li[x-i][y-i]=='W':
            k+=1
            i+=1
        elif li[x-i][y-i]=='B':
            n+=k
            break
    return n
def column(x,y):
    global ln
    n=0
    k=0
    for i in range(y+1,ln):
        if li[x][i]=='.':break
        elif li[x][i]=='W':k+=1
        elif li[x][i]=='B':
            n+=k
            break
    k=0
    for i in range(y-1,-1,-1):
        if li[x][i]=='.':break
        elif li[x][i]=='W':k+=1
        elif li[x][i]=='B':
            n+=k
            break
    return n
def row(x,y):
    global ln
    n=0
    k=0
    for i in range(x+1,ln):
        if li[i][y]=='.':break
        elif li[i][y]=='W':k+=1
        elif li[i][y]=='B':
            n+=k
            break
    k=0
    for i in range(x-1,-1,-1):
        if li[i][y]=='.':break
        elif li[i][y]=='W':k+=1
        elif li[i][y]=='B':
            n+=k
            break
    return n
def num(x,y):
    return row(x,y)+column(x,y)+cross(x,y)
ln=int(input())
li=[list(input()) for _ in range(ln)]
can=[]
for i in range(ln):
    for j in range(ln):
        if li[i][j]=='.':
            can.append((i,j))
ans=[[-num(i,j),i,j] for i,j in can]
ans.sort()
if ans[0][0]==0:
    print('PASS')
else:
    print(ans[0][2],ans[0][1])
    print(-ans[0][0])