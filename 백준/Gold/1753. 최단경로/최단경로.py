from heapq import *
import sys
read = sys.stdin.readline

V, E = map(int, read().rstrip().split())
K = int(read().rstrip())
GRAPH = [[*map(int, read().rstrip().split())] for _ in range(E)]

# 1. Set Graph
graph = [[] for _ in range(V+1)]
for a, b, dist in GRAPH:
  graph[a].append([dist, b])

# 2. Set Distance
distance = [float('inf') for _ in range(V+1)]
distance[K] = 0

# 3. BFS
queue = [[0, K]]
heapify(queue)
while queue:
  dist, to = heappop(queue)

  if distance[to] < dist: continue

  for step_dist, step_to in graph[to]:
    new_dist = dist + step_dist
    if distance[step_to] > new_dist:
      distance[step_to] = new_dist
      heappush(queue, [new_dist, step_to])

print("\n".join(map(str, map(lambda x: "INF" if (x == float('inf')) else str(x), distance[1:]))))
# print("\n".join(map(str, distance[1:])))
