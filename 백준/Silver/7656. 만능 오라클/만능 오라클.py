s=input()
li=[]
now=0
for i in range(len(s)):
    if s[i]=='.':
        li.append(s[now:i+1].strip())
        now=i+1
    elif s[i]=='?':
        li.append(s[now:i+1].strip())
        now=i+1
li=list(map(lambda x:x.split(),filter(lambda x:x[-1]=='?',li)))
for i in range(len(li)):
    for j in range(len(li[i])):
        if li[i][j]=='What':
            li[i][j]='Forty-two'
        elif li[i][j][-1]=='?':
            new=li[i][j][:-1]+'.'
            li[i][j]=new
for i in map(lambda x:' '.join(x),li):print(i)