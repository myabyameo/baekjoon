t=[13,7,5,3,3,2]
li=list(map(int,input().split()))
a=sum(t[i]*li[i] for i in range(6))
li=list(map(int,input().split()))
b=sum(t[i]*li[i] for i in range(6))+1.5
if a>b:print('cocjr0208')
else:print('ekwoo')