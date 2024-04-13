from heapq import *
import sys
read = sys.stdin.readline

N, D = map(int, read().rstrip().split())
ROAD = [[*map(int, read().rstrip().split())] for _ in range(N)]

graph = [[] for _ in range(D+1)]

for i in range(D):
    graph[i].append((i+1, 1))

for s, e, dist in ROAD:
    if e > D: continue
    graph[s].append([e, dist])

INF = 987654321
distance = [INF]*(D+1)
distance[0] = 0

queue = [[0, 0]]
heapify(queue)
while queue:
    d, now = heappop(queue)
    if distance[now] < d: continue

    for x in graph[now]:
        dist = d + x[1]
        if distance[x[0]] > dist:
            distance[x[0]] = dist
            heappush(queue, (dist, x[0]))

print(distance[D])