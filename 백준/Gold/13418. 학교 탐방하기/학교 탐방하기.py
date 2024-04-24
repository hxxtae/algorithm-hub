import sys
read = sys.stdin.readline

N, M = [*map(int, read().rstrip().split())]
GRAPH  = [[*map(int, read().rstrip().split())] for _ in range(M+1)]

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

def runMST(desc):
  parent = [i for i in range(N+1)]
  graph = sorted(GRAPH, key=lambda x: -x[2] if desc else x[2])
  cnt = 0
  for a, b, val in graph:
    if not findParent(a, b, parent):
      unionParent(a, b, parent)
      if val == 0:
        cnt += 1
      
  return cnt

good = runMST(True) ** 2
bad = runMST(False) ** 2
print(bad - good)
