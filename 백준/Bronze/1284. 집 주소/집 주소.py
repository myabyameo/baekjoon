while True:
    s=input()
    if s=='0':break
    ans=0
    for i in s:
        if i=='1':ans+=2
        elif i=='0':ans+=4
        else:ans+=3
    print(ans+len(s)+1)