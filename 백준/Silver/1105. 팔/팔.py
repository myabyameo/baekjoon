m, M = input().split()
n=0
if len(M)>len(m):
 print(0)
else:
 for i in range(len(m)):
  if m[i]==M[i]=='8':n+=1
  if m[i]!=M[i]:break
 print(n)