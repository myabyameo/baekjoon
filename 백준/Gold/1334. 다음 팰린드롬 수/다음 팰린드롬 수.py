s=input()
l=len(s)
if l==1:
    s=int(s)+1
    if s==10:
        s+=1
elif l%2!=0:
    li=s[:l//2]
    t=s[l//2+1:]
    m=s[l//2]
    if int(li[::-1])<=int(t):
        if s[l//2]!='9':
            s=li+str(int(m)+1)+li[::-1]
        else:
            if len(str(int(li)+1))==len(li):
                s=str(int(li)+1)+'0'+str(int(li)+1)[::-1]
            else:
                s=str(int(li)+1)+str(int(li)+1)[::-1]
    else:
        s=li+m+li[::-1]
else:
    li=s[:l//2]
    t=s[l//2:]
    if int(li[::-1])<=int(t):
        if len(li)==len(str(int(li)+1)):
            s=str(int(li)+1)+str(int(li)+1)[::-1]
        else:
            s=str(int(li)+1)+str(int(li)+1)[::-1][1:]
    else:
        s=li+li[::-1]
print(s)