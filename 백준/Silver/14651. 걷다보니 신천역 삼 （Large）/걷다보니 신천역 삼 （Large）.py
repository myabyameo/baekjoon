p=10**9+9
n=[0]*33334
n[2]=2
n[3]=6
for i in range(4,33334):
    n[i]=n[i-1]*3%p
print(n[int(input())])