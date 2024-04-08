from collections import deque
import sys
read = sys.stdin.readline

N, M, R = map(int, read().rstrip().split(' '))
ARR = [[*map(int, read().rstrip().split(' '))] for _ in range(M)]

graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)

for a, b in ARR:
  graph[a].append(b)
  graph[b].append(a)

for arr in graph:
  arr.sort()

def bfs(startNode):
  cnt = 1
  queue = deque([startNode])
  visited[startNode] = cnt
  
  while queue:
    node = queue.popleft()
    
    for next in graph[node]:
      if visited[next]: continue
      visited[next] = cnt + 1
      queue.append(next)
      cnt += 1

bfs(R)
print("\n".join(map(str, visited[1:])))
