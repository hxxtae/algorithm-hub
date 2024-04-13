from sys import setrecursionlimit
import sys
read = sys.stdin.readline
setrecursionlimit(10 ** 6)

N, M, R = [*map(int, read().rstrip().split())]
GRAPH = [[*map(int, read().rstrip().split())] for _ in range(M)]

visited = [0] * (N+1)
graph = [[] for _ in range(N+1)]
cnt = 1

def dfs(node):
  if visited[node]: return
  global cnt
  visited[node] = cnt
  cnt += 1

  for next in graph[node]:
    dfs(next)

for a, b in GRAPH:
  graph[a].append(b)
  graph[b].append(a)

for add in graph:
  add.sort(key=lambda x: -x)

dfs(R)
print("\n".join(map(str, visited[1:])))
