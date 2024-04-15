import sys
read = sys.stdin.readline

N, M = map(int, read().rstrip().split())
CAMPUS = read().rstrip().split()
GRAPH = [[*map(int, read().rstrip().split())] for _ in range(M)]

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

parent = [i for i in range(N+1)]
graph = sorted(GRAPH, key=lambda x: x[2])
answer = 0
for a, b, val in graph:
  if CAMPUS[a-1] == CAMPUS[b-1]: continue
  if not findParent(a, b, parent):
    unionParent(a, b, parent)
    answer += val

for i in range(1, N+1):
  getParent(i, parent)

if len(set(parent[1:])) == 1:
  print(answer)
else:
  print(-1)
