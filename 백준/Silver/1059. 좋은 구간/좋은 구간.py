t = int(input())
L = list(map(int,input().split()))
L.append(0)
L.sort()
n = int(input())
for i in range(len(L)-1):
  if L[i] < n < L[i+1]:
    print((n-L[i])*(L[i+1]-n)-1)
    break
  elif L[i] == n or L[i+1] == n:
    print(0)
    break