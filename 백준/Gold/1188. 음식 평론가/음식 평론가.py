def gcd(a,b):
    if a%b:return gcd(b,a%b)
    return b
a,b=map(int,input().split())
g=gcd(a,b)
print(b-g)