import sys
n=int(sys.stdin.readline())
if n==1:
    print('1/1')
else:
    s=3; i=2; s2=1
    for i in range(2, n):
        if s2<n<=s:
            break
        s2+=i
        i+=1
        s+=i
    if i%2==1:
        print(f'{s-n+1}/{i-s+n}')
    else:
        print(f'{i-s+n}/{1+s-n}')