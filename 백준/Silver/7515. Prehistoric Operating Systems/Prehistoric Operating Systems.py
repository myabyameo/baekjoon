li=[2,3]
for i in range(40):
    li.append(li[-1]+li[-2])
for _ in range(int(input())):
    n=int(input())
    print(f'Scenario {_+1}:\n{li[n-1]}\n')