a = 3
while a != 0:
  n = int(input())
  t = []
  for i in range(n):
    t.append(int(input()))
  result = sum(t)
  if result == 0:
    print("0")
  elif result >0:
    print("+")
  elif result < 0:
    print("-")
  a-=1