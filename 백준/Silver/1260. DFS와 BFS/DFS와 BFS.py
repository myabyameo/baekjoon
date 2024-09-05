#줄이 많을 수 있기에 stdin.readline() 사용
from collections import deque
from sys import *
n, m, v = map(int, stdin.readline().rstrip().split())
t = [[0]*(n+1) for i in range(n+1)] # 1 0 들어가는거
vi = [0]*(n+1)
vi2 = [0]*(n+1)
#노드 번호를 그대로 인덱스로 사용하려는 경우 리스트 크기를 n+1개로 잡기
# 방문..처리!!..?!??
for b in range(m): #반복은 for문으로
    x, y = map(int, stdin.readline().rstrip().split())
    t[x][y] = 1
    t[y][x] = 1
def dfs(a):
    vi[a] = 1
    print(a, end=' ')
    for i in range(1,n+1):
        if vi[i] == 0 and t[a][i] == 1: #방문리스트 확인 / 연결 여부 확인
            dfs(i)
dfs(v)


def bfs(a):
    q = deque()
    q.append(a)
    vi2[a] = 1
    while q:
        a = q.popleft()
        print(a, end=' ')
        for i in range(1, n+1):
            if vi2[i] == 0 and t[a][i] == 1:
                q.append(i)
                vi2[i] = 1
print()
bfs(v)