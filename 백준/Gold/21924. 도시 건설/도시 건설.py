from functools import reduce
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
maxPrice = reduce(lambda sum, curr: sum + curr[2], GRAPH, 0)
minPrice = 0

GRAPH.sort(key=lambda x: x[2])
for a, b, val in GRAPH:
  if not findParent(a, b, parent):
    unionParent(a, b, parent)
    minPrice += val

for i in range(1, N+1):
  getParent(i, parent)

confirm = all(parent[1] == i for i in parent[1:])
if(confirm):
  print(maxPrice - minPrice)
else:
  print(-1)

