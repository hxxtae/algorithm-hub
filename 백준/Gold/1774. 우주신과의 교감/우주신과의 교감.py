import math
import sys
read = sys.stdin.readline

def distanceAtoB(pos1, pos2):
  x1, y1 = pos1
  x2, y2 = pos2
  a = x1 - x2
  b = y1 - y2
  return float(math.sqrt((a * a) + (b * b)))

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

N, M = map(int, read().rstrip().split())
N_POS = [list(map(int, read().rstrip().split())) for _ in range(N)]
M_POS = [list(map(int, read().rstrip().split())) for _ in range(M)]

parent = [i for i in range(N)]
M_POS.sort()
for a, b in M_POS:
  if not findParent(a-1, b-1, parent):
    unionParent(a-1, b-1, parent)

graph = []
for r in range(N-1):
  for c in range(r+1, N):
    val = distanceAtoB(N_POS[r], N_POS[c])
    graph.append((val, r, c))

graph.sort()

answer = 0
for val, a, b in graph:
  if not findParent(a, b, parent):
    unionParent(a, b, parent)
    answer += val

print('%.2f' %(answer))
