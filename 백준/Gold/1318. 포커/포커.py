def gcd(a,b):
    if a%b:return gcd(b,a%b)
    return b
ans=[6612900, 9730740, 2532816, 732160, 282060, 39780, 39780, 205976, 165984, 14664, 1472, 188]
s=sum(ans)
for i in ans:
    g=gcd(i,s)
    print(f'{i//g}/{s//g}')