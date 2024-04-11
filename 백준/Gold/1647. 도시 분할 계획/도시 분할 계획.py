import sys
read = sys.stdin.readline

N, M = [*map(int, read().rstrip().split())]
GRAPH = [[*map(int, read().rstrip().split())] for _ in range(M)]

graph = sorted(GRAPH, key=lambda x: x[2])
parent = [i for i in range(N+1)]

def getParent(x, parent):
  return x if parent[x] == x else getParent(parent[x], parent)

def unionParent(x, y, parent):
  a, b = [getParent(x, parent), getParent(y, parent)]
  if a < b: parent[b] = a
  else: parent[a] = b

def findParent(x, y, parent):
  a, b = [getParent(x, parent), getParent(y, parent)]
  if a == b: return True
  return False

answer = []
for a, b, val in graph:
  if not findParent(a, b, parent):
    unionParent(a, b, parent)
    answer.append(val)

print(sum(answer[:-1]))