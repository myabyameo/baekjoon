n=0
for i in range(8):
    s=input()
    if i%2:
        for j in range(1,8,2):
            if s[j]=='F':n+=1
    else:
        for j in range(0,8,2):
            if s[j]=='F':n+=1
print(n)