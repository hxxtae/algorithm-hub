from collections import deque
import sys
read = sys.stdin.readline

def solution(n, d, c, arr):
  # 1. Set Graph
  graph = [[] for _ in range(n+1)]
  for a, b, dist in arr:
    graph[b].append([a, dist])
  
  # 2. Set Distance
  distance = [float('inf')] * (n+1)
  distance[c] = 0

  # 3. BFS
  queue = deque([[c, 0]])
  while queue:
    to, dist = queue.popleft()
    
    if distance[to] < dist: continue
    
    for step_to, step_dist in graph[to]:
      new_dist = dist + step_dist
      if distance[step_to] > new_dist:
        distance[step_to] = new_dist
        queue.append([step_to, new_dist])
  
  answer = list(filter(lambda x: isinstance(x, int), distance))
  print(len(answer), max(answer))

T = int(read().rstrip())
for _ in range(T):
  N, D, C = map(int, read().rstrip().split())
  ARR = [[*map(int, read().rstrip().split())] for _ in range(D)]
  solution(N, D, C, ARR)