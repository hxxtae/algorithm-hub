from collections import deque
import sys
read = sys.stdin.readline

N, M, X = map(int, read().rstrip().split())
GRAPH = [[*map(int, read().rstrip().split())] for _ in range(M)]

# 1. Set Graph
graph = [[] for _ in range(N+1)]
for a, b, dist in GRAPH:
  graph[a].append((b, dist))

def dijkstraFunc(start):
  # 2. Set Distance
  distance = [float('inf') for _ in range(N+1)]
  distance[start] = 0

  # 3. BFS
  queue = deque([[start, 0]])
  while queue:
    to, dist = queue.popleft()
    
    if distance[to] < dist: continue

    for step_to, step_dist in graph[to]:
      new_dist = dist + step_dist
      if distance[step_to] > new_dist:
        distance[step_to] = new_dist
        queue.append([step_to, new_dist])
  
  return distance

# - 각 정점(마을)에서 부터 X까지의 최단거리
startToX = []
for i in range(1, N+1):
  distArr = dijkstraFunc(i)
  startToX.append(distArr[X])

# - X정점(마을)에서 각 정점까지의 최단거리
xToEnd = dijkstraFunc(X)[1:]

# 출력
answer = max([startToX[i] + xToEnd[i] for i in range(N)])
print(answer)