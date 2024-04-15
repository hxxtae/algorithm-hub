from collections import deque
import sys
read = sys.stdin.readline

N = int(read().rstrip())
M = int(read().rstrip())
ARR = [[*map(int, read().rstrip().split())] for _ in range(M)]
S, E = map(int, read().rstrip().split())

# 1. Set Graph
graph = [[] for _ in range(N+1)]
for a, b, dist in ARR:  
  graph[a].append([b, dist])

# 2. Set Distance
distance = [float('inf')] * (N+1)
distance[S] = 0

# 3. BFS
queue = deque([[S, 0]])
while queue:
  to, dist = queue.popleft()

  if distance[to] < dist: continue

  for step_to, step_dist in graph[to]:
    new_dist = dist + step_dist
    if distance[step_to] > new_dist:
      distance[step_to] = new_dist
      queue.append([step_to, new_dist])

print(distance[E])
