import heapq
import sys
#input = sys.stdin.readline

n = int(input())  
m = int(input())  
t = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    t[a].append((b, c))  
s, e = map(int, input().split())  
def dijkstra(t, s):
    distances = [int(1e9)] * (n+1) 
    distances[s] = 0  
    queue = []
    heapq.heappush(queue, [distances[s], s]) 

    while queue:  
        dist, node = heapq.heappop(queue)  
        if distances[node] < dist:
            continue

        for next_node, next_dist in t[node]:
            distance = dist + next_dist 
            if distance < distances[next_node]: 
                distances[next_node] = distance
                heapq.heappush(queue, [distance, next_node])  
    return distances

dist_start = dijkstra(t, s)
print(dist_start[e])