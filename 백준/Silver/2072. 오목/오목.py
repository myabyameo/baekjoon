def check1(stone,x,y):
    num=0
    n=x
    m=y
    while 0<=n<19 and 0<=m<19 and omok[n][m]==stone:
        n+=1
        num+=1
    n=x-1
    m=y
    while 0<=n<19 and 0<=m<19 and omok[n][m]==stone:
        n-=1
        num+=1
    if num==5:return True
    return False
def check2(stone,x,y):
    num=0
    n=x
    m=y
    while 0<=n<19 and 0<=m<19 and omok[n][m]==stone:
        m+=1
        num+=1
    n=x
    m=y-1
    while 0<=n<19 and 0<=m<19 and omok[n][m]==stone:
        m-=1
        num+=1
    if num==5:return True
    return False
def check3(stone,x,y):
    num=0
    n=x
    m=y
    while 0<=n<19 and 0<=m<19 and omok[n][m]==stone:
        n+=1
        m+=1
        num+=1
    n=x-1
    m=y-1
    while 0<=n<19 and 0<=m<19 and omok[n][m]==stone:
        n-=1
        m-=1
        num+=1
    if num==5:return True
    return False
def check4(stone,x,y):
    num=0
    n=x
    m=y
    while 0<=n<19 and 0<=m<19 and omok[n][m]==stone:
        n+=1
        m-=1
        num+=1
    n=x-1
    m=y+1
    while 0<=n<19 and 0<=m<19 and omok[n][m]==stone:
        n-=1
        m+=1
        num+=1
    if num==5:return True
    return False
n=int(input())
li=[list(map(int,input().split())) for _ in range(n)]
if n<=8:print(-1)
else:
    real=True
    omok=[[0 for _ in range(19)] for _ in range(19)]
    for ind,t in enumerate(li):
        t[0]-=1
        t[1]-=1
        if ind%2==0:
            omok[t[0]][t[1]]=1
            if check1(1,t[0],t[1]) or check2(1,t[0],t[1]) or check3(1,t[0],t[1]) or check4(1,t[0],t[1]):
                print(ind+1)
                real=False
                break
        else:
            omok[t[0]][t[1]]=2
            if check1(2,t[0],t[1]) or check2(2,t[0],t[1]) or check3(2,t[0],t[1]) or check4(2,t[0],t[1]):
                print(ind+1)
                real=False
                break
    if real:print(-1)