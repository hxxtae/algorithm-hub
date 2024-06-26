from heapq import *
import sys
read = sys.stdin.readline

N = int(read().rstrip())
FRIENDS = [*map(int, read().rstrip().split())]
M = int(read().rstrip())
GRAPH = [[*map(int, read().rstrip().split())] for _ in range(M)]

# 1. Set Graph
graph = [[] for _ in range(N+1)]
for a, b, dist in GRAPH:
  graph[a].append([dist, b])
  graph[b].append([dist, a])

def onDijkstra():
  # 2. Set Distance
  distance = [float('inf')] * (N+1)
  heap = []
  for i in FRIENDS:
    distance[i] = 0
    heap.append([0, i]) # [dist, start_node]
  
  # 3. BFS
  heapify(heap)
  while heap:
    dist, to = heappop(heap)

    if distance[to] < dist: continue

    for step_dist, step_to in graph[to]:
      new_dist = step_dist + dist
      if new_dist < distance[step_to]:
        distance[step_to] = new_dist
        heappush(heap, [new_dist, step_to])
  
  return distance

distList = onDijkstra()

answer = 0
maxDist = 0
for i in range(1, N+1):
  if maxDist < distList[i]:
    maxDist = distList[i]
    answer = i

print(answer)
