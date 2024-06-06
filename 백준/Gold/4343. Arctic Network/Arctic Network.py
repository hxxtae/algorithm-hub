import math
import sys
read = sys.stdin.readline

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

def getDistance(x1, y1, x2, y2):
  return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def mstModule(s, p, p_list):
  if (s - p) == 1:
    print(0)
    return
  parent = [i for i in range(p)]
  graph = []
  for i in range(p):
    for j in range(1+i, p):
      dist = getDistance(*p_list[i], *p_list[j])
      graph.append((dist, i, j))
  
  graph.sort()
  
  answer = 0
  cnt = 0
  for dist, a, b in graph:
    if not findParent(a, b, parent):
      unionParent(a, b, parent)
      answer = '{:.2f}'.format(dist)
      cnt += 1
      if cnt == (p-s): break

  print(answer)
  
N = int(read().rstrip())
for _ in range(N):
  S, P = map(int, read().rstrip().split())
  P_LIST = [[*map(int, read().rstrip().split())] for _ in range(P)]
  mstModule(S, P, P_LIST)
