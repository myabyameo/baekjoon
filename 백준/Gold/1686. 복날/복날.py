import sys
from collections import deque
f=lambda a,b,c,d:(b-a)**2+(d-c)**2
a,b=map(int,sys.stdin.readline().split())
a*=60
a*=b
a**=2
start_x,start_y=map(float,sys.stdin.readline().split())
end_x,end_y=map(float,sys.stdin.readline().split())
bunkers=[]
num=0
while True:
    try:
        s=sys.stdin.readline().strip()
        if not s:break
        bunkers.append(list(map(float,s.split()))+[num]);num+=1
    except:break
bunkers.append([end_x,end_y,bunkers[-1][-1]+1])
visit=[True]*len(bunkers)
deq=deque()
deq.append((start_x,start_y,0))
real=False
while deq:
    c,k,n=deq.popleft()
    if c==end_x and k==end_y:
        ans=n-1
        real=True
        break
    for i,j,num in bunkers:
        if f(c,i,k,j)<=a and visit[num]:
            visit[num]=False
            deq.append([i,j,n+1])
if real:print(f'Yes, visiting {ans} other holes.')
else:print('No.')