from itertools import combinations
dic={f'{i}rmt':i for i in range(10)}
for i in range(1,11):
    dic[f'{i}eod']=i+9
a,b=map(int,input().split())
li=[i for i in range(1,11)]*2
li.remove(a)
li.remove(b)
if a==b:
    whrqh=dic[f'{a}eod']
else:
    whrqh=dic[f'{(a+b)%10}rmt']
total=0
ans=0
for i,j in combinations(li,2):
    total+=1
    if i==j:
        if dic[f'{i}eod']<whrqh:ans+=1
    else:
        if dic[f'{(i+j)%10}rmt']<whrqh:ans+=1
print('%.3f' %(ans/total))