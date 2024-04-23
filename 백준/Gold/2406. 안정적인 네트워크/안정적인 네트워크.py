import sys
read = sys.stdin.readline

N, M = map(int, read().rstrip().split())
GRAPH = [[*map(int, read().rstrip().split())] for _ in range(M)]
MATRIX = [[*map(int, read().rstrip().split())] for _ in range(N)]

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
for a, b in GRAPH:
  if not findParent(a, b, parent):
    unionParent(a, b, parent)

graph = []
for r in range(1, N):
  for c in range(r+1, N):
    graph.append([r+1, c+1, MATRIX[r][c]])
graph.sort(key=lambda x: x[2])

kinds = []
answer = 0
for a, b, val in graph:
  if not findParent(a, b, parent):
    unionParent(a, b, parent)
    answer += val
    kinds.append(f"{a} {b}")

print(answer, len(kinds))
print("\n".join(kinds))