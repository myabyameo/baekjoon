import sys
def chai(a,b):
    t=0
    for i in range(8):
        if a[i]!=b[i]:t+=1
    return t
a,b=map(int,sys.stdin.readline().split())
t=[['WBWBWBWB','BWBWBWBW'],['BWBWBWBW','WBWBWBWB']]
li=[0]*a
for i in range(a):
    li[i]=sys.stdin.readline().strip()
ans=[]
for i in range(a-8+1):
    for j in range(b-8+1):
        c=0
        for k in range(i,i+8):
            c+=chai(li[k][j:j+8],t[0][(k-i)%2])
        ans.append(c)
        c=0
        for k in range(i,i+8):
            c+=chai(li[k][j:j+8],t[1][(k-i)%2])
        ans.append(c)
print(min(ans))