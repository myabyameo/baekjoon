s=list(input())
s=list(map(lambda x:int(x),s))
s.sort()
s=s[::-1]
s=list(map(lambda x:str(x),s))
print(''.join(s))