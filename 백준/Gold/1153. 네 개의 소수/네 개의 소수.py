k=10**6+1
che=[True]*k
prime=[]
for i in range(2,k):
    if che[i]:
        prime.append(i)
        for j in range(i+i,k,i):
            che[j]=False
n=int(input())
if n<8:
    print(-1)
else:
    ans=[2]
    if n%2:
        ans.append(3)
        n-=5
    else:
        ans.append(2)
        n-=4
    for i in prime:
        if che[n-i]:
            ans.append(i)
            ans.append(n-i)
            break
    ans.sort()
    print(*ans)