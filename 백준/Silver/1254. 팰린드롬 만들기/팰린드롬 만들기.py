n=input()
l=len(n)
for i in range(l):
    st=n[i:]
    if st==st[::-1]:
        break
print(l+i)