s=input()
l=len(s)
ans=[]
for i in range(l-2):
    for j in range(i+1,l-1):
        ans.append(''.join([s[:i+1][::-1],s[i+1:j+1][::-1],s[j+1:][::-1]]))
ans.sort()
print(ans[0])