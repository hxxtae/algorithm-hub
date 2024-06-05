import sys
read = sys.stdin.readline

N = int(read().rstrip())
GRAPH = [[*map(int, read().rstrip().split())] for _ in range(N)]

def getParent(x, parent):
  if x != parent[x]:
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

def getDistance(x1, y1, x2, y2):
  return ((x1 - x2)**2 + (y1 - y2)**2)

parent = [i for i in range(N+1)]
graph = []
for i in range(N):
  for j in range(1+i, N):
    graph.append((getDistance(*GRAPH[i], *GRAPH[j]), i+1, j+1))

graph.sort()

answer = 0
cnt = 0
for dist, a, b in graph:
  if not findParent(a, b, parent):
    unionParent(a, b, parent)
    answer = max(answer, dist)
    cnt += 1
    if cnt == N-1: break

print(answer)