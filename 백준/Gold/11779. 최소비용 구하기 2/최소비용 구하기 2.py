from heapq import *
import sys
read = sys.stdin.readline

N = int(read().rstrip())
M = int(read().rstrip())
GRAPH = [[*map(int, read().rstrip().split())] for _ in range(M)]
S, E = map(int, read().rstrip().split())

# 1. Set Graph
graph = [[] for _ in range(N+1)]
for a, b, dist in GRAPH:
  graph[a].append((dist, b))

# 2. Set Distance
distance = [float('inf') for _ in range(N+1)]
distance[S] = 0

# 3. BFS
history = [0] * (N+1)
heap = [(0, S)]
heapify(heap)
while heap:
  dist, to = heappop(heap)

  if distance[to] < dist: continue
  
  for step_dist, step_to in graph[to]:
    new_dist = dist + step_dist
    if distance[step_to] > new_dist:
      distance[step_to] = new_dist
      heappush(heap, (new_dist, step_to))
      history[step_to] = to

dist_path = [E]
now = E
while now != S:
  now = history[now]
  dist_path.append(now)

dist_path.reverse()
print(distance[E])
print(len(dist_path))
print(*dist_path)
