from collections import deque
import sys
read = sys.stdin.readline

V, E, P = map(int, read().rstrip().split())
GRAPH = [[*map(int, read().rstrip().split())] for _ in range(E)]

# 1. Set Graph
graph = [[] for _ in range(V+1)]
for a, b, dist in GRAPH:
  graph[a].append((dist, b))
  graph[b].append((dist, a))

# 3. BFS
def bfs(startNode):
  # 2. Set Distance
  distance = [float('inf') for _ in range(V+1)]
  distance[1] = 0

  queue = deque([(0, startNode)]) # (dist, node)
  while queue:
    dist, to = queue.popleft()

    if distance[to] < dist: continue

    for step_dist, step_to in graph[to]:
      new_dist = dist + step_dist
      if distance[step_to] > new_dist:
        distance[step_to] = new_dist
        queue.append((new_dist, step_to))
  
  return distance

dist1toV = bfs(1)
distPtoV = bfs(P)
if dist1toV[V] < dist1toV[P] + distPtoV[V]:
  print("GOOD BYE")
else:
  print("SAVE HIM")