def one(a,b):
    if a%2==0:
        return False
    return True
for _ in range(int(input())):
    a,b,c=map(int,input().split())
    if c==0:
        if a==0:
            if b==0:print('No')
            elif b%2:print('No')
            else:print('Yes')
        else:
            if a%2:
                print('No')
            else:
                print('Yes')
    elif c==1:
        if one(a,b):
            print('Yes')
        else:
            print('No')
    else:
        if a<=c-1:
            print('No')
        else:
            a-=c-1
            c=1
            if one(a,b):
                print('Yes')
            else:print('No')