dic={'0':'O','1':'L','2':'Z','3':'E','5':'S','6':'B','7':'T','8':'B'}
a,b=map(int,input().split())
li=[0]*a
for i in range(a):
    li[i]=input()
for _ in range(b):
    s=list(input())
    for i in range(len(s)):
        s[i]=dic.get(s[i],s[i])
    s=''.join(s)
    check=0
    for i in li:
        if i not in s:
            check+=1
    if check==a:
        print('VALID')
    else:print('INVALID')