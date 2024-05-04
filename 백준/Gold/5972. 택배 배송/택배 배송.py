from heapq import *
import sys
read = sys.stdin.readline

N, M = map(int, read().rstrip().split())
GRAPH = [[*map(int, read().rstrip().split())] for _ in range(M)]

# 1. Set graph
graph = [[] for _ in range(N+1)]
for a, b, dist in GRAPH:
  graph[a].append([dist, b])
  graph[b].append([dist, a])

# 2. Set Distance
distance = [float('inf') for _ in range(N+1)]
distance[1] = 0

# 3. BFS
heap = [[0, 1]] # [dist, to]
heapify(heap)
while heap:
  dist, to = heappop(heap)
  
  if distance[to] < dist: continue
  
  for step_dist, step_to in graph[to]:
    new_dist = dist + step_dist
    if distance[step_to] > new_dist:
      distance[step_to] = new_dist
      heappush(heap, [new_dist, step_to])

print(distance[N])