import sys
t=0
for i in range(int(sys.stdin.readline())):
    dic=dict()
    s=sys.stdin.readline().strip()
    for i in list(set(s)):
        dic[i]=[]
    dic[s[0]]=[0]
    for i in range(1,len(s)):
        if s[i-1]==s[i]:
            continue
        else:
            dic[s[i]].append(i)
    real=True
    for i in dic.values():
        if len(i)>1:
            real=False
    if real:
        t+=1
print(t)