s ="1234567890-=WERTYUIOP[]SDFGHJKL;'XCVBNM,./ "
s2='`1234567890-QWERTYUIOP[ASDFGHJKL;ZXCVBNM,. '
dic={s[i]:s2[i] for i in range(len(s))}
while True:
    try:
        s=input()
    except:
        break
    ans=[]
    for i in s:
        ans.append(dic.get(i,']'))
    print(''.join(ans))