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

parent = [i for i in range(N+1)]
graph = []
for r in range(N):
  for c in range(r+1, N):
    graph.append((GRAPH[r][c], r+1, c+1))

graph.sort()

answer = 0
linkArr = []
for dist, a, b in graph:
  
  if not findParent(a, b, parent):
    unionParent(a, b, parent)
    answer += abs(dist)
    if dist > 0: linkArr.append((a, b))
  else:
    if dist < 0: answer += abs(dist)

print(answer, len(linkArr))
for arr in linkArr:
  print(*arr)
