earth=0
pl=0
other=0
n=int(input())
for i in range(n):
    s=input()
    if 'black' in s and 'blue' in s:
        earth+=1
    elif 'white' in s and 'gold' in s:
        pl+=1
    else:
        other+=1
print(earth/n*100)
print(pl/n*100)
print(other/n*100)