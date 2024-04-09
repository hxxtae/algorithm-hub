from collections import deque
import sys
read = sys.stdin.readline

N, M = map(int, read().rstrip().split())
BRIDGE = [[*map(int, read().rstrip().split())] for _ in range(M)]
S, E = map(int, read().rstrip().split())
minS = 0
maxE = 1000000000

graph = [[] for _ in range(N+1)]
for a, b, k in BRIDGE:
  graph[a].append([b, k])
  graph[b].append([a, k])

def bfs(weight):
  queue = deque([S])
  visited = [0] * (N+1)
  visited[S] = 1

  while queue:
    x = queue.popleft()

    if x == E: return True
    
    for nextX, nextK in graph[x]:
      if visited[nextX]: continue
      if nextK < weight: continue
      visited[nextX] = 1
      queue.append(nextX)

  return False

answer = 0
while minS <= maxE:
  half = (minS + maxE) // 2
  
  result = bfs(half)

  if result:
    minS = half + 1
    answer = half
  else:
    maxE = half - 1

print(answer)
