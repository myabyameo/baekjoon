import sys
def fib(n,p):
    t = [[1, 1], [1, 0]]

    def wow(a, b):
        if b != 1:
            u = wow(a, b // 2)
            if b % 2 != 0:
                return hehe(hehe(u, u), a)
            else:
                return hehe(u, u)
        else:
            return a

    def hehe(a, b):
        w = [[0] * 2 for _ in range(2)]
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    w[i][j] += a[i][k] * b[k][j] % p
        return w

    result = wow(t, n)

    return result[0][1] % p
while True:
    n=int(sys.stdin.readline())
    if n==0:
        print(0)
    elif n==-1:
        break
    else:
        print(fib(n,10000))