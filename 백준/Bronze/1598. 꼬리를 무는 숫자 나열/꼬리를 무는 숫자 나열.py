d, s= map(int, input().split())
d = d-1
s = s-1
print(abs(d // 4 - s// 4) + abs(d% 4 - s% 4))