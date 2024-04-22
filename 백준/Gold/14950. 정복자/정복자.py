import sys
read = sys.stdin.readline

N, M, T = map(int, read().rstrip().split())
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

graph = sorted(GRAPH, key=lambda x: x[2])
parent = [i for i in range(N+1)]
answer = 0
price = 0

for a, b, val in graph:
  if not findParent(a, b, parent):
    unionParent(a, b, parent)
    answer += val
    answer += price
    price += T

print(answer)