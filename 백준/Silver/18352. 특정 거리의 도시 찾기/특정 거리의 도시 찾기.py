from collections import deque
import sys
read = sys.stdin.readline

N, M, K, X = map(int, read().rstrip().split())
GRAPH = [[*map(int, read().rstrip().split())] for _ in range(M)]

# 1. Set Graph
graph = [[] for _ in range(N+1)]

for a, b in GRAPH:
  graph[a].append([b, 1])

# 2. Set Distance
distance = [float('inf')] * (N+1)
distance[X] = 0

# 3. BFS
queue = deque([[X, 0]])
while queue:
  to, dist = queue.popleft()

  if distance[to] < dist: continue
  
  for step_to, step_dist in graph[to]:
    new_dist = distance[to] + step_dist
    if distance[step_to] > new_dist:
      distance[step_to] = new_dist
      queue.append([step_to, new_dist])

answer = list(map(lambda item: item[0]+1, filter(lambda x: x[1] == K, enumerate(distance[1:]))))
if answer:
  print("\n".join(map(str, answer)))
else:
  print(-1)
  
