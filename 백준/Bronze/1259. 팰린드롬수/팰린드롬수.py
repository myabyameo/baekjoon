while True:
  a = input()
  t = []
  t2 = []
  if a == "0":
    break
  else:
    t = list(a)
    t2 = t[::-1]
    if t == t2:
      print("yes")
    else:
      print("no")