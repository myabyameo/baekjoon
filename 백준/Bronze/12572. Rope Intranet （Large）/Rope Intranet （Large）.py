for _ in range(int(input())):
    n=int(input())
    li=[0]*n
    for i in range(n):
        li[i]=list(map(int,input().split()))
    ans=0
    for i in range(n):
        for j in range(i+1,n):
            if (li[i][0]-li[j][0])*(li[i][1]-li[j][1])<0:
                ans+=1
    print(f'Case #{_+1}: {ans}')