def um(li):
    n=0
    if li[0][0]==li[1][1]==li[2][2]==li[3][3]==li[4][4]==0:
        n+=1
    if li[0][4]==li[1][3]==li[2][2]==li[3][1]==li[4][0]==0:
        n+=1
    return n
def row(li):
    n=0
    for i in range(5):
        if li[0][i]==li[1][i]==li[2][i]==li[3][i]==li[4][i]==0:
            n+=1
    return n
def col(li):
    n=0
    for i in range(5):
        if li[i][0]==li[i][1]==li[i][2]==li[i][3]==li[i][4]==0:
            n+=1
    return n
def line(li):
    return col(li)+row(li)+um(li)
li=[list(map(int,input().split())) for _ in range(5)]
t=list(map(int,input().split()))+list(map(int,input().split()))+list(map(int,input().split()))+list(map(int,input().split()))+list(map(int,input().split()))
for i in range(25):
    real=False
    for x in range(5):
        for y in range(5):
            if li[x][y]==t[i]:
                li[x][y]=0
                real=True
                break
        if real:break
    if line(li)>=3:
        print(i+1)
        break