def column(n):
    if len({li[i][n] for i in range(9)})==9:
        return True
    return False
def row(n):
    if len(set(li[n]))==9:
        return True
    return False
def box(x,y):
    se=set()
    d=[0,1,2]
    for i in d:
        for j in d:
            se.add(li[x+i][y+j])
    if len(se)==9:
        return True
    return False
n=int(input())
for i in range(1,n+1):
    li=[0]*9
    for j in range(9):
        li[j]=list(map(int,input().split()))
    check=0
    for j in range(9):
        if column(j):check+=1
        if row(j):check+=1
    for j in range(3):
        for k in range(3):
            if box(j*3,k*3):check+=1
    if check==27:
        print(f'Case {i}: CORRECT')
    else:
        print(f'Case {i}: INCORRECT')
    if i!=n:input()