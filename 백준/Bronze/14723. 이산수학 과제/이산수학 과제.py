from bisect import bisect_left
li=[1]
n=1
while li[-1]<=1000:li.append(li[-1]+n);n+=1
n=int(input())
ind=bisect_left(li,n)
if li[ind]>n:
    ind-=1
a=ind+1
b=1
a-=n-li[ind]
b+=n-li[ind]
print(a,b)