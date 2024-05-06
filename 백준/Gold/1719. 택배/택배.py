from heapq import *
import sys
read = sys.stdin.readline

N, M = map(int, read().rstrip().split())
GRAPH = [[*map(int, read().rstrip().split())] for _ in range(M)]

# 1. Set Graph
graph = [[] for _ in range(N+1)]
for a, b, dist in GRAPH:
  graph[a].append([dist, b])
  graph[b].append([dist, a])


def dijkstraFunc(start):
  # 2. Set Distance
  distance = [float('inf')] * (N+1)
  distance[start] = 0

  prevNodes = ['-'] * (N+1)

  # 3. BFS
  heap = [[0, start]]
  heapify(heap)
  while heap:
    dist, to = heappop(heap)

    if distance[to] < dist: continue

    for step_dist, step_to in graph[to]:
      new_dist = dist + step_dist
      if distance[step_to] > new_dist:
        distance[step_to] = new_dist
        heappush(heap, [new_dist, step_to])
        prevNodes[step_to] = to
  
  matrix.append(prevNodes[1:])

matrix = []
for i in range(1, N+1):
  dijkstraFunc(i)

for r in range(N):
  for c in range(N):
    print(matrix[c][r], end=' ')
  print()