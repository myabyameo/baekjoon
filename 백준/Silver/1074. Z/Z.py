def find(a,b,i):
    if a<=1 and b<=1:
        li=[[0,1],[2,3]]
        return li[a][b]
    add=0
    if a>=2**i:
        add+=2**(2*i+1)
        a-=2**i
    if b>=2**i:
        add+=2**(i*2)
        b-=2**i
    return find(a,b,i-1)+add
a,b,c=map(int,input().split())
print(find(b,c,a-1))