a,b=map(int,input().split())
li=[0]*a
for i in range(a):
    li[i]=list(map(int,input().split()))
    if li[i][0]==b:
        gold=li[i][1]
        silver=li[i][2]
        bronze=li[i][3]
li.sort(key=lambda x:x[3],reverse=True)
li.sort(key=lambda x:x[2],reverse=True)
li.sort(key=lambda x:x[1],reverse=True)
n=0
for i,j,k,l in li:
    if j==gold and k==silver and l==bronze:
        break
    n+=1
print(n+1)