a,b,c=map(int,input().split())
d,e,f=map(int,input().split())
if a+b*2+c*3>d+e*2+f*3:print(1)
elif a+b*2+c*3==d+e*2+f*3:print(0)
else:print(2)