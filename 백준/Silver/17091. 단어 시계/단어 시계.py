dic={
    0:'twelve',
    1:'one',
    2:'two',
    3:'three',
    4:'four',
    5:'five',
    6:'six',
    7:'seven',
    8:'eight',
    9:'nine',
    10:'ten',
    11:'eleven',
    12:'twelve',
    13:'thirteen',
    14:'fourteen',
    15:'quarter',
    16:'sixteen',
    17:'seventeen',
    18:'eighteen',
    19:'nineteen',
    20:'twenty',
}
h=int(input())
m=int(input())
if m==0:
    print(f"{dic[h]} o' clock")
elif m==30:
    print(f"half past {dic[h]}")
elif m<30:
    if m<=20:
        if m==15:
            print(f"{dic[m]} past {dic[h]}")
        elif m==1:
            print(f"{dic[m]} minute past {dic[h]}")
        else:
            print(f"{dic[m]} minutes past {dic[h]}")
    else:
        print(f'twenty {dic[m%10]} minutes past {dic[h]}')
else:
    m=60-m
    if m<=20:
        if m==15:
            print(f"{dic[m]} to {dic[(h+1)%12]}")
        elif m==1:
            print(f"{dic[m]} minute to {dic[(h+1)%12]}")
        else:
            print(f"{dic[m]} minutes to {dic[(h+1)%12]}")
    else:
        print(f"twenty {dic[m%10]} minutes to {dic[(h+1)%12]}")