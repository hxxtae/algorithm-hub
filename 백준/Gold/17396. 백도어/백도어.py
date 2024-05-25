from heapq import *
import sys
read = sys.stdin.readline

N, M = map(int, read().rstrip().split())
WAD = [*map(int, read().rstrip().split())]
GRAPH = [[*map(int, read().rstrip().split())] for _ in range(M)]

# 1. Set Graph
graph = [[] for _ in range(N)]
for a, b, dist in GRAPH:
  graph[a].append((dist, b))
  graph[b].append((dist, a))

# 2. Set Distance
distance = [float("inf")] * N
distance[0] = 0

# 3. BFS
heap = [[0, 0]] # [dist, node]
heapify(heap)
while heap:
  dist, to = heappop(heap)

  if distance[to] < dist: continue
  if WAD[to] == 1 and (to != (N-1)): continue

  for step_dist, step_to in graph[to]:
    new_dist = dist + step_dist
    if distance[step_to] > new_dist:
      distance[step_to] = new_dist
      heappush(heap, [new_dist, step_to])

if type(distance[N-1]) == int:
  print(distance[N-1])
else:
  print(-1)

