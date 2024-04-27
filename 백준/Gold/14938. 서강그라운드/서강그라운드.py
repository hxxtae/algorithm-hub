from collections import deque
import sys
read = sys.stdin.readline

N, M, R = map(int, read().rstrip().split())
ARR_T = [*map(int, read().rstrip().split())]
GRAPH = [[*map(int, read().rstrip().split())] for _ in range(R)]

# 1. Set graph
graph = [[] for _ in range(N+1)]
for a, b, dist in GRAPH:
  graph[a].append([b, dist])
  graph[b].append([a, dist])

def dijkstraRun(start):
  # 2. Set distance
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

answer = 0
for i in range(N):
  arrIdx = [*map(lambda y: y[0], filter(lambda x: x[1] <= M, enumerate(dijkstraRun(i+1)[1:])))]
  total = 0
  for idx in arrIdx:
    total += ARR_T[idx] # + 낙하산에서 내린 지점의 아이템 수 + 내린 곳에서 수색 범위 이하인 최단거리를 만족하는 지점의 아이템의 개수
  answer = max(answer, total)

print(answer)