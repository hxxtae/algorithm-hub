from heapq import *
import sys
read = sys.stdin.readline

N, M, K = map(int, read().rstrip().split())
GRAPH = [[*map(int, read().rstrip().split())] for _ in range(M)]
STARTS = list(map(int, read().rstrip().split()))

# 1. Set Graph
graph = [[] for _ in range(N+1)]
for a, b, dist in GRAPH:
  graph[b].append((dist, a))

# 2. Set Distance
heap = []
distance = [float('inf')] * (N+1)
for i in STARTS:
  distance[i] = 0
  heap.append((0, i)) # (dist, start_node)

# 3. BFS
heapify(heap)
while heap:
  dist, to = heappop(heap)

  if distance[to] < dist: continue

  for step_dist, step_to in graph[to]:
    new_dist = step_dist + dist
    if new_dist < distance[step_to]:
      distance[step_to] = new_dist
      heappush(heap, (new_dist, step_to))

max_node, max_dist = 0, 0
for i in range(1, N+1):
  dist = distance[i]
  if max_dist < dist:
    max_node = i
    max_dist = dist

print(max_node)
print(max_dist)