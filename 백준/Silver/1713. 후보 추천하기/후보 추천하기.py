n=int(input())
k=int(input())
li=list(map(int,input().split()))
dic=dict()
t=[]
for i in li:
    if i in dic:
        dic[i]+=1
    else:
        if len(t)<n:
            t.append(i)
            dic[i]=1
        else:
            minor=[]
            m=max(dic.values())
            for k,j in dic.items():
                if j<m:
                    minor=[]
                    minor.append(k)
                    m=j
                elif j==m:
                    minor.append(k)
            for j in range(len(t)):
                if t[j] in minor:
                    k=t[j]
                    del t[j]
                    t.append(i)
                    dic[i]=1
                    dic.pop(k)
                    break
print(*sorted(t))