import sys
m, n = map(int, sys.stdin.readline().split())
a = set(map(int, sys.stdin.readline().split()))
b = set(map(int, sys.stdin.readline().split()))
print(len((a-b)|(b-a)))