import sys
l=int(sys.stdin.readline())
r=int(sys.stdin.readline())
k=int(sys.stdin.readline())
n=0
if k==2:
  if l<=3:
    l=3
  n=r-l+1
if k==3:
  for i in range(l, r+1):
    if i%3==0 and i!=3:
      n+=1
if k==4:
  for i in range(l, r+1):
    if i>=10 and i!=12 and i%2==0:
      n+=1
if k==5:
  for i in range(l, r+1):
    if i>=15 and i%5==0:
      n+=1
print(n)