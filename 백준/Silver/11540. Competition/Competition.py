a,b,c=map(int,input().split())
li=sorted(list(map(int,input().split())))
t=sorted(list(map(int,input().split())))
ans=0
now=-1
while li and t:
    if li[0]<t[0]:
        if now==-1:
            now=0
            li.pop(0)
        elif now==0:
            li.pop(0)
        elif now==1:
            li.pop(0)
            ans+=1
            now=0
    elif li[0]==t[0]:
        li.pop(0)
        t.pop(0)
    elif li[0]>t[0]:
        if now==-1:
            now=1
            t.pop(0)
        elif now==0:
            ans+=1
            t.pop(0)
            now=1
        elif now==1:
            t.pop(0)
if (not li) and t:
    if now==0:ans+=1
elif li and (not t):
    if now==1:ans+=1
print(ans)