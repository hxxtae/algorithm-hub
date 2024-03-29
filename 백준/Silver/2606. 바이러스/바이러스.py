import sys
rl = sys.stdin.readline

N = int(rl().rstrip())
K = int(rl().rstrip())

graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)

for _ in range(K):
  a, b = map(int, rl().rstrip().split(' '))
  graph[a].append(b)
  graph[b].append(a)

def dfs(node, cnt):
  for next in graph[node]:
    if visited[next]: continue
    visited[next] = 1
    cnt = dfs(next, cnt + 1)
  
  return cnt

visited[1] = 1
print(dfs(1, 0))