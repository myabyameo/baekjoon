a,b = map(str, input().split())
a1 = list(a)
b1 = list(b)
a1 = list(map(int, a1))
b1 = list(map(int, b1))
sum = 0
for i in a1:
  for j in b1:
    sum = sum+i*j
print(sum)