for _ in range(int(input())):
    a,b,c=input().split()
    dic={}
    for i in a+b+c:
        if i in dic.keys():
            dic[i]+=1
        else:
            dic[i]=1
    if len(set(dic.values()))==1:
        a=int(a)
        b=int(b)
        c,d=int(c[:2]),int(c[2:])
        if a==b+c+d or b==a+c+d or c==a+b+d or d==a+b+c or a+b==c+d or a+c==b+d or a+d==b+c:
            print('yes')
        else:
            print('no')
    else:
        print('no')