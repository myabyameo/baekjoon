import sys
input=sys.stdin.readline
s=input()
li=[dict() for _ in range(len(s)+1)]
for i in range(len(s)):
    li[i+1]=li[i].copy()
    if s[i] in li[i]:
        li[i+1][s[i]]+=1
    else:
        li[i+1][s[i]]=1
for _ in range(int(input())):
    a,b,c,d=map(int,input().split())
    dic1={}
    for i,j in li[b].items():
        if j-li[a-1].get(i,0)==0:continue
        dic1[i]=j-li[a-1].get(i,0)
    dic2={}
    for i,j in li[d].items():
        if j-li[c-1].get(i,0)==0:continue
        dic2[i]=j-li[c-1].get(i,0)
    if dic1==dic2:
        print('DA')
    else:
        print('NE')