n=int(input())
li=[0]*n
for i in range(n):
    li[i]=list(map(int,input().split()))
li.sort(key=lambda x:x[0])
print(li[n//2][0] if n%2 else li[n//2-1][0],end=' ')
li.sort(key=lambda x:x[1])
print(li[n//2][1] if n%2 else li[n//2-1][1])