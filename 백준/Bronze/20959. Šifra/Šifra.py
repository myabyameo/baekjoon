s=list(input())
for i in range(len(s)):
    if s[i].isalpha():
        s[i]=' '
s=''.join(s)
print(len(set(s.split())))