import sys
m,M=map(int,sys.stdin.readline().split())
n=M-m+1
che=[True]*n
for i in range(2,int(M**0.5)+1):
    square=i*i
    for j in range((((m-1)//square)+1)*square,M+1,square):
        if che[j-m]:
            che[j-m]=False
            n-=1
print(n)