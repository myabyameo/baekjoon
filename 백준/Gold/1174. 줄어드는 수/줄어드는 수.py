from itertools import combinations
n=int(input())-1
li=[]
for i in range(1,11):
    for j in combinations(range(0,10),i):
        j=list(j)
        j.sort(reverse=True)
        li.append(''.join(map(str,j)))
li=list(map(int,li))
li.sort()
try:
    print(li[n])
except:
    print(-1)