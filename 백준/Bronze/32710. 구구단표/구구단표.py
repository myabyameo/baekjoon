check=[False]*101
for i in range(1,10):
    for j in range(1,10):
        check[i*j]=True
print(int(check[int(input())]))