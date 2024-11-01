import sys
from math import ceil
input=sys.stdin.readline
for _ in range(int(input())):
    n,m=map(int,input().split())
    cars=dict()
    for i in range(n):
        a,b,c,d=input().split()
        cars[a]=[int(b),int(c),int(d)]
    dic=dict()
    for i in range(m):
        a,b,c,d=input().split()
        if b in dic:
            dic[b].append([int(a),c,d])
        else:
            dic[b]=[[int(a),c,d]]
    ans=dict()
    for i in dic:
        real=True
        skip=False
        dic[i].sort(key=lambda x:x[0])
        ans[i]=0
        pickup_num,ret_num=0,0
        for j in dic[i]:
            if j[1]=='p':
                if not real:
                    skip=True
                    break
                else:
                    ans[i]+=cars[j[2]][1]
                    now_car=j[2]
                    real=False
                    pickup_num+=1
            elif j[1]=='a':
                if real:
                    skip=True
                    break
                else:
                    ans[i]+=ceil(cars[now_car][0]*int(j[2])/100)
            elif j[1]=='r':
                if real:
                    skip=True
                    break
                else:
                    ans[i]+=cars[now_car][2]*int(j[2])
                    real=True
                    ret_num+=1
        if skip or pickup_num!=ret_num:
            ans[i]='INCONSISTENT'
            continue
    li_ans=[[i,ans[i]] for i in ans]
    li_ans.sort(key=lambda x:x[0])
    for i,j in li_ans:
        print(i,j)