dic={'L':0,'O':0,'V':0,'E':0}
n=input()
for i in ['L','O','V','E']:
    dic[i]+=n.count(i)
ans=-1
name=''
li=[]
for i in range(int(input())):
    li.append(input())
li.sort()
for s in li:
    l=s.count('L')+dic['L']
    o=s.count('O')+dic['O']
    v=s.count('V')+dic['V']
    e=s.count('E')+dic['E']
    if ans<((l+o)*(l+v)*(l+e)*(o+v)*(o+e)*(v+e))%100:
        ans=((l+o)*(l+v)*(l+e)*(o+v)*(o+e)*(v+e))%100
        name=s
print(name)