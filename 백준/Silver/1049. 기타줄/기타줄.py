import sys
n,m=map(int,sys.stdin.readline().split())
six=[]
one=[]
for i in range(m):
    a,b=map(int,sys.stdin.readline().split())
    six.append(a)
    one.append(b)
a=min(six)
b=min(one)
biyong=[]
for i in range(n//6+2):
    k=a*i+(n-i*6)*b
    if n-i*6>=0:
        biyong.append(a*i+(n-i*6)*b)
    else:
        biyong.append(a*i)
print(min(biyong))