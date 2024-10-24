while True:
    q = input()
    if q == "#":
        break
    o = 0
    for i in q:
        i=i.lower()
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
            o += 1
    print(o)