import sys
n=int(sys.stdin.readline())
li=[0]*n
for i in range(n):
    li[i]=sys.stdin.readline().strip()
d={x:0 for x in list(set(li))}
for i in li:
    d[i]+=1
t1=list(d.keys())
t2=list(d.values())
ans=[]
for i in range(len(d)):
    ans.append([t1[i],t2[i]])
ans.sort(key=lambda x:x[0])
ans.sort(key=lambda x:-x[1])
print(ans[0][0])