p=1000000009
li=[0]*(100001)
li[0]=1
li[1]=1
li[2]=2
li[3]=2
li[4]=3
li[5]=3
li[6]=6
for i in range(7,100001):
    li[i]=(li[i-2]+li[i-4]+li[i-6])%p
for i in range(int(input())):
    print(li[int(input())])