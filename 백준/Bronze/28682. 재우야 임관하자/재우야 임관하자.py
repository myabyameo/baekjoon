import sys
n=int(sys.stdin.readline())
li=['swimming' for _ in range(n)]
sys.stdout.write(' '.join(li)+'\n')
sys.stdout.flush()
dic={'bowling':'soccer','soccer':'bowling'}
t=sys.stdin.readline().strip().split()
ans=[0]*n
for i in range(n):
    ans[i]=dic[t[i]]
sys.stdout.write(' '.join(ans)+'\n')
sys.stdout.flush()