from heapq import *
import sys
read = sys.stdin.readline

N, E = map(int, read().rstrip().split())
GRAPH = [[*map(int, read().rstrip().split())] for _ in range(E)]
NODE1, NODE2 = map(int, read().rstrip().split())

# 1. Set Graph
graph = [[] for _ in range(N+1)]
for a, b, dist in GRAPH:
  graph[a].append([dist, b])
  graph[b].append([dist, a])

def dijkstra(start):
  # 2. Set Distance
  distance = [float('inf') for _ in range(N+1)]
  distance[start] = 0

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

  return distance

# 1에서 Node1, Node2까지의 최단거리 중 최소값
dist1 = dijkstra(1)

# Node1에서 Node2까지의 최단거리 (양방향 이므로 Node2에서 Node1 까지의 거리와 같다.)
dist2 = dijkstra(NODE1)[NODE2]

# N에서 Node1, Node2까지의 최단거리 중 최소값
dist3 = dijkstra(N)

answer1 = dist1[NODE1] + dist2 + dist3[NODE2]
answer2 = dist1[NODE2] + dist2 + dist3[NODE1]

if answer1 == float('inf') and answer2 == float('inf'):
  print(-1)
else:
  print(min(answer1, answer2))