import sys
read = sys.stdin.readline

def getParent(x, parent):
  return x if parent[x] == x else getParent(parent[x], parent)

def unionParent(x, y, parent):
  a, b = [getParent(x, parent), getParent(y, parent)]
  if a > b: parent[a] = b
  else: parent[b] = a

def findParent(x, y, parent):
  a, b = [getParent(x, parent), getParent(y, parent)]
  if a == b: return True
  return False

def mstFunc(m, graph):
  graph = sorted(graph, key=lambda x: x[2])
  parent = [i for i in range(m)]
  total = sum([arr[2] for arr in graph])

  answer = 0
  for a, b, val in graph:
    if not findParent(a, b, parent):
      unionParent(a, b, parent)
      answer += val

  return (total - answer)

while True:
  M, N = map(int, read().rstrip().split())
  if M == 0 and N == 0: break
  GRAPH = [[*map(int, read().rstrip().split())] for _ in range(N)]

  print(mstFunc(M, GRAPH))
