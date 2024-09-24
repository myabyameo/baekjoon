from collections import deque
n=int(input())
li=list(map(int,input().split()))
deq=deque(li)
waiting=deque()
now=1
while now<n:
    if deq:
        c=deq.popleft()
        if c==now:
            now+=1
        else:
            if waiting:
                k=waiting.pop()
                if k==now:
                    now+=1
                    deq.appendleft(c)
                else:
                    waiting.append(k)
                    waiting.append(c)
            else:
                waiting.append(c)
    else:
        if waiting:
            c=waiting.pop()
            if c==now:
                now+=1
            else:
                break
        else:
            break
print('Nice' if n==now else 'Sad')