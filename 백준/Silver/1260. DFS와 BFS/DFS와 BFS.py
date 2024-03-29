import sys
rl = sys.stdin.readline

N, M, V = map(int, rl().rstrip().split(' '))

graph = [[] for _ in range(N+1)]
visitedDFS = [0] * (N+1)
visitedBFS = [0] * (N+1)
answer = []
for _ in range(M):
  a, b = map(int, rl().rstrip().split(' '))
  graph[a].append(b)
  graph[b].append(a)

for i in range(N + 1):
  graph[i].sort()

# DFS
def dfs(node):
  if visitedDFS[node]:
    return
  
  answer.append(node)
  visitedDFS[node] = 1
  for next in graph[node]:
    dfs(next)

# BFS
def bfs():
  queue = [V]
  visitedBFS[V] = 1
  answer = []

  while len(queue):
    node = queue.pop(0)
    answer.append(node)
    
    for next in graph[node]:
      if visitedBFS[next]: continue
      visitedBFS[next] = 1
      queue.append(next)
  
  return answer

dfs(V)
print(*answer)
print(*bfs())