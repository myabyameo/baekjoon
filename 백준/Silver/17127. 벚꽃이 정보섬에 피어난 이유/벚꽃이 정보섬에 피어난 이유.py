n=int(input())
li=input().split()
print(max(eval('*'.join(li[:i+1]))+eval('*'.join(li[i+1:j+1]))+eval('*'.join(li[j+1:k+1]))+eval('*'.join(li[k+1:])) for i in range(n-3) for j in range(i+1,n-2) for k in range(j+1,n-1)))