a=int(input())
b=sum(map(int,input().split()))
if a<=240 or a<=b:
    print('high speed rail')
else:print('flight')