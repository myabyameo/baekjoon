k = []
while True:
  sum = 0
  a = input()
  if a == "#":
    break
  else:
    k = list(a)
    for i in k:
      if i == "a":
        sum += 1
      elif i == 'e':
        sum += 1
      elif i == 'i':
        sum += 1
      elif i == 'o':
        sum += 1
      elif i == 'u':
        sum += 1
      elif i == "A":
        sum += 1
      elif i == "E":
        sum += 1
      elif i == "I":
        sum += 1
      elif i == "O":
        sum += 1
      elif i == "U":
        sum += 1
  print(sum)