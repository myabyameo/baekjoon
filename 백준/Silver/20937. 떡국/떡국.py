n=int(input())
li=list(map(int,input().split()))
dic={}
for i in li:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
print(max(dic.values()))