import sys
read = sys.stdin.readline

N, M = map(int, read().rstrip().split())
GRAPH = [[*map(int, read().rstrip().split())] for _ in range(M)]

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
graph = sorted(GRAPH, key=lambda x: (-x[3], -x[2]))

answer = sum([i[2] for i in graph])
for a, b, c, _ in graph:
  if not findParent(a, b, parent):
    unionParent(a, b, parent)
    answer -= c

print(answer)