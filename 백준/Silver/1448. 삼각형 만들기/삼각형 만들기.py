n = int(input())
gili = []
for i in range(n):
    gili.append(int(input()))
gili.sort()
t = [-1]
for i in range(1, n-1):
    if gili[-i]<gili[-i-1]+gili[-i-2]:
        t.append(gili[-i]+gili[-i-1]+gili[-i-2])
        break
print(t[-1])