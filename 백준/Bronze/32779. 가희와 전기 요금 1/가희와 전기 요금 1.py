from decimal import Decimal as D
for _ in range(int(input())):
    a,b=map(D,input().split())
    print(int(a*b*D('105.6')/D('60000')))