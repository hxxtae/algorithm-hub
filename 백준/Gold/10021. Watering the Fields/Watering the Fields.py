from heapq import *
import sys
read = sys.stdin.readline

N, C = map(int, read().rstrip().split())
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

def getExpence(xi, yi, xj, yj):
  return abs((xj - xi) ** 2) + abs((yj - yi) ** 2)

parent = [i for i in range(N)]
graph = []
heapify(graph)
for i in range(N):
  for j in range(i+1, N):
    dist = getExpence(*GRAPH[i], *GRAPH[j])
    if dist >= C: 
      heappush(graph, (dist, i, j))

answer = 0
cnt = 0
while graph:
  dist, a, b = heappop(graph)
  if not findParent(a, b, parent):
    unionParent(a, b, parent)
    answer += dist
    cnt += 1
    if cnt == (N-1): break

if cnt >= (N-1):
  print(answer)
else:
  print(-1)
