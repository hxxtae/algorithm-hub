from sys import setrecursionlimit
import sys
read = sys.stdin.readline

N, M, R = map(int, read().rstrip().split(' '))
ARR = [[*map(int, read().rstrip().split(' '))] for _ in range(M)]

setrecursionlimit(10 ** 6)
graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)

for a, b in ARR:
  graph[a].append(b)
  graph[b].append(a)

for arr in graph:
  arr.sort()

def dfs(node, cnt):
  if visited[node]: return cnt
  cnt += 1
  visited[node] = cnt
  
  for next in graph[node]:
    cnt = dfs(next, cnt)
  
  return cnt

dfs(R, 0)
print("\n".join(map(str, visited[1:])))