n = int(input())
dap = []
for _ in range(n):
    a, b = map(int, input().split())
    a=a%10
    b=b%4
    if b==0:
        b=4
    if a==0:
        dap.append(10)
    else:
        dap.append((a**b)%10)
for i in dap:
    print(i)