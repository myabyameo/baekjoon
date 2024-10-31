from math import exp,log,e
while True:
    li=input().split()
    if li[0]=='E':break
    if 'T' in li and 'D' in li:
        for i in range(3):
            if li[i]=='T':
                T=float(li[i+1])
            elif li[i]=='D':
                D=float(li[i+1])
        H=T+0.5555*(6.11*exp(5417.7530*(1/273.16-1/(273.16+D)))-10)
        print('T',T,'D',D,'H',round(H,1))
    elif 'T' in li and 'H' in li:
        for i in range(3):
            if li[i]=='T':
                T=float(li[i+1])
            elif li[i]=='H':
                H=float(li[i+1])
        h=H-T
        e2=10+h/0.5555
        D=1/(1/273.16-log(e2/6.11,e)/5417.7530)-273.16
        print('T',T,'D',round(D,1),'H',H)
    elif 'D' in li and 'H' in li:
        for i in range(3):
            if li[i]=='D':
                D=float(li[i+1])
            if li[i]=='H':
                H=float(li[i+1])
        e2=6.11*exp(5417.7530*(1/273.16-1/(273.16+D)))
        h=0.5555*(e2-10)
        T=H-h
        print('T',round(T,1),'D',D,'H',H)