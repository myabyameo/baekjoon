# 1010번 다리 놓기

def factorial(k):  # factorial 정의
  d = 1
  for i in range(1, k+1):
    d*=i
  return d
  
t = int(input()) # 테스트 케이스 t
for i in range(t): # 테스트 케이스 반복
  n, m = map(int, input().split())  # 각각 n, m : 사이트 개수
  print(factorial(m)//((factorial(n)*factorial(m-n)))) # H(n,r)씀