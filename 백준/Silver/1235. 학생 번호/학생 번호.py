import sys
n = int(sys.stdin.readline())
number = []
end_of_number = []
for i in range(n):
    a = input()
    number.append(a)
a=len(a)
for i in range(a):
    for j in number:
        end_of_number.append(int(j[a-i-1:]))
    if n == len(set(end_of_number)):
        print(i+1)
        break
    else:
        end_of_number = []