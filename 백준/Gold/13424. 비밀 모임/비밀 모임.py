from collections import deque, defaultdict
import sys
read = sys.stdin.readline

T = int(read().rstrip())
for _ in range(T):
  N, M = map(int, read().rstrip().split())
  GRAPH = [[*map(int, read().rstrip().split())] for _ in range(M)]
  K = int(read().rstrip())
  K_LIST = list(map(int, read().rstrip().split()))

  # 1. Set Graph
  graph = [[] for _ in range(N+1)]
  for a, b, dist in GRAPH:
    graph[a].append((dist, b))
    graph[b].append((dist, a))
  
  def onDijkstra(startNode):
    # 2. Set Distance
    distance = [float('inf') for _ in range(N+1)]
    distance[startNode] = 0

    # 3. BFS
    queue = deque([(0, startNode)]) # dist, node
    while queue:
      dist, to = queue.popleft()

      if distance[to] < dist: continue

      for step_dist, step_to in graph[to]:
        new_dist = dist + step_dist
        if new_dist < distance[step_to]:
          distance[step_to] = new_dist
          queue.append((new_dist, step_to))
    
    return distance
  
  answerObj = defaultdict(int)
  for start in K_LIST:
    answerDist = onDijkstra(start)
    for idx, minDist in enumerate(answerDist):
      answerObj[idx] += minDist
  
  print(min(answerObj, key=answerObj.get))