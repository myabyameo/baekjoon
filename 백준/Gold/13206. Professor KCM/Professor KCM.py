import sys
che=[i for i in range(1001)]
for i in range(2,1001):
    if che[i]==i:
        for j in range(i+i,1001,i):
            che[j]=che[i]
for _ in range(int(sys.stdin.readline())):
    n=int(sys.stdin.readline())
    li=list(map(int,sys.stdin.readline().split()))
    dic={}
    for i in li:
        t={}
        while i>1:
            if che[i] in t:
                t[che[i]]+=1
            else:
                t[che[i]]=1
            i//=che[i]
        for j in t:
            dic[j]=max(dic.get(j,0),t[j])
    ans=1
    p=10**9+7
    for i in dic:
        ans*=i**dic[i]
        ans%=p
    print(ans)