def div(k,i,n):
    if i==0:
        if n==1:print('m')
        else:print('o')
    else:
        if n<=(k-i-3)//2:
            div((k-i-3)//2,i-1,n)
        elif (k-i-3)//2<n<=k-(k-i-3)//2:
            n-=(k-i-3)//2
            if n==1:print('m')
            else:print('o')
        elif k-(k-i-3)//2<n:
            div((k-i-3)//2,i-1,n-(k-(k-i-3)//2))
i=0
k=3
n=int(input())
while k<n:
    k=k*2+i+4
    i+=1
div(k,i,n)