import sys
input = sys.stdin.readline
channel=int(input())
broken_num=int(input())
if broken_num==0:
    print(min(len(str(channel)), abs(channel-100)))
else:
    button = list(input().split())
    count=abs(channel-100)
    for i in range(1000001):
        st=str(i)
        for j in range(len(st)):
            if st[j] in button:
                break
        else:
            count=min(count, abs(i-channel)+len(str(i)))
    print(count)