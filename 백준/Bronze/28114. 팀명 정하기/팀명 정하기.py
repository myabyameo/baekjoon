li1=input().split()
li2=input().split()
li3=input().split()
li1[0]=int(li1[0]);li1[1]=int(li1[1])
li2[0]=int(li2[0]);li2[1]=int(li2[1])
li3[0]=int(li3[0]);li3[1]=int(li3[1])
t=[li1,li2,li3]
t.sort(key=lambda x:x[1])
ans=''
for i in t:
    ans+=str(i[1]%100)
print(ans)
t.sort(key=lambda x:x[0],reverse=True)
ans=''
for i in t:
    ans+=i[-1][0]
print(ans)