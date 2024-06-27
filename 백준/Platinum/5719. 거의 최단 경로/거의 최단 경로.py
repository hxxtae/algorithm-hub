from heapq import *
from collections import deque
import sys
read = sys.stdin.readline

while True:
  N, M = map(int, read().rstrip().split())
  if N == 0 and M == 0: break
  S, D = map(int, read().rstrip().split())
  GRAPH = [[*map(int, read().rstrip().split())] for _ in range(M)]

  # 1. Set Graph
  graph = [[] for _ in range(N)]
  graph_reverse = [[] for _ in range(N)]
  for a, b, dist in GRAPH:
    graph[a].append([dist, b]) # 단방향 (정방향)
    graph_reverse[b].append([dist, a]) # 단방향 (역방향)
  
  edges = [[False] * N for _ in range(N)]
  
  def onDijkstra():
    # 2. Set Distance
    distance = [float('inf')] * N
    distance[S] = 0

    # 3. BFS
    heap = [[0, S]] # [dist, start_node]
    heapify(heap)
    while heap:
      dist, to = heappop(heap)

      if distance[to] < dist: continue

      for step_dist, step_to in graph[to]:
        new_dist = dist + step_dist
        if edges[to][step_to]: continue
        if new_dist < distance[step_to]:
          distance[step_to] = new_dist
          heappush(heap, [new_dist, step_to])

    return distance
  
  def BFS():
    queue = deque([D])

    while queue:
      step_to = queue.popleft()

      if step_to == S: continue

      for dist, to in graph_reverse[step_to]:
        # step_to로 향하는 이전 간선 비용을 사용했을 때 distances에 기록된 비용이라면 곧 최단 경로에 사용했다는 뜻이다.
        if distance[step_to] == (distance[to] + dist) and not edges[to][step_to]:
          edges[to][step_to] = True
          queue.append(to)

  distance = onDijkstra()
  BFS()
  distance = onDijkstra()

  if distance[D] == float('inf'):
    print(-1)
  else:
    print(distance[D])