from heapq import *
import sys
read = sys.stdin.readline

N, M, K = map(int, read().rstrip().split())
GRAPH = [[*map(int, read().rstrip().split())] for _ in range(M)]

# 1. Set Graph
graph = [[] for _ in range(N+1)]
for a, b, dist in GRAPH:
  graph[a].append((dist, b))

# 2. Set Distance (heapq)
distance = [[] for _ in range(N+1)]
heappush(distance[1], 0)

# 3. BFS
heap = [(0, 1)] # (start_dist, start_node)
heapify(heap)
while heap:
  dist, to = heappop(heap)

  for step_dist, step_to in graph[to]:
    new_dist = dist + step_dist
    
    # distance의 heapq 길이가 K보다 작을 때
    if len(distance[step_to]) < K:
      heappush(distance[step_to], -new_dist)
      heappush(heap, (new_dist, step_to))
    # disrance의 heapq 길이가 K와 같아지고, new_dist 값(비용)이 더 작을 때
    elif -distance[step_to][0] > new_dist:
      heappop(distance[step_to])
      heappush(distance[step_to], -new_dist)
      heappush(heap, (new_dist, step_to))

for hq in distance[1:]:
  if len(hq) == K:
    print(-hq[0])
  else: 
    print(-1)
