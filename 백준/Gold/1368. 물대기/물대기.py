from heapq import *
import sys
read = sys.stdin.readline

N = int(read().rstrip())
WELL = [int(read().rstrip()) for _ in range(N)]
GRAPH = [[*map(int, read().rstrip().split())] for _ in range(N)]

def getParent(x, parent):
  if parent[x] != x:
    parent[x] = getParent(parent[x], parent)
  return parent[x]

def unionParent(x, y, parent):
  a, b = [getParent(x, parent), getParent(y, parent)]
  if a > b: parent[a] = b
  else: parent[b] = a

def findParent(x, y, parent):
  a, b = [getParent(x, parent), getParent(y, parent)]
  if a == b: return True
  return False

# - 물기을 만들어 물을 대는 비용들
graph = []
for r in range(N):
  for c in range(r+1, N):
    graph.append([r+1, c+1, GRAPH[r][c]])

# - 우물을 파는 비용들
for i in range(N):
  graph.append([0, i+1, WELL[i]])
graph.sort(key=lambda x: x[2])

parent = [i for i in range(N+1)]
answer = 0
for a, b, val in graph:
  if not findParent(a, b, parent):
    unionParent(a, b, parent)
    answer += val

print(answer)
