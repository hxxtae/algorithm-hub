from heapq import *
import sys
read = sys.stdin.readline

V, E = map(int, read().rstrip().split())
GRAPH = [[*map(int, read().rstrip().split())] for _ in range(E)]

M, M_LIMIT = map(int, read().rstrip().split())
M_LIST = list(map(int, read().rstrip().split()))
S, S_LIMIT = map(int, read().rstrip().split())
S_LIST = list(map(int, read().rstrip().split()))

graph = [[] for _ in range(V+1)]
for a, b, dist in GRAPH:
  graph[a].append([dist, b])
  graph[b].append([dist, a])

heapOfM = []
heapOfS = []
distanceOfM = [float('inf')] * (V+1)
distanceOfS = [float('inf')] * (V+1)
for i in M_LIST:
  distanceOfM[i] = 0
  heapOfM.append([0, i]) # dist, node
for i in S_LIST:
  distanceOfS[i] = 0
  heapOfS.append([0, i]) # dist, node

def onDijkstra(heap, distance):
  heapify(heap)
  while heap:
    dist, to = heappop(heap)

    if distance[to] < dist: continue

    for step_dist, step_to in graph[to]:
      new_dist = dist + step_dist
      if new_dist < distance[step_to]:
        distance[step_to] = new_dist
        heappush(heap, [new_dist, step_to])

onDijkstra(heapOfM, distanceOfM)
onDijkstra(heapOfS, distanceOfS)

answer = float('inf')
for i in range(V+1):
  if i in M_LIST or i in S_LIST: continue
  if distanceOfM[i] > M_LIMIT or distanceOfS[i] > S_LIMIT: continue
  answer = min(answer, distanceOfM[i] + distanceOfS[i])

if answer == float('inf'):
  print(-1)
else:
  print(answer)
