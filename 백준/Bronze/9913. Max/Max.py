n=int(input())
dic={}
for i in range(n):
    a=int(input())
    if a in dic:
        dic[a]+=1
    else:
        dic[a]=1
print(max(dic.values()))