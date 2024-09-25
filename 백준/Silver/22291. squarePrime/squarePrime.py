def isPrime(n):
    if n<=1:return False
    return all(n%i for i in range(2,int(n**0.5)+1))

def isSquare(n):
    if n<=0:return False
    return n==int(n**0.5)**2

def P2(A):
    ans=0
    for i,j in enumerate(A):
        if isPrime(i) and isSquare(j):
            ans+=j
    return ans
