from collections import deque
import sys
read = sys.stdin.readline

N, M, K = map(int, read().rstrip().split())
graph = [[*map(int, read().rstrip().split()), i+1] for i in range(M)]

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

def confirmMST(parent):
  for i in range(1, N+1):
    getParent(i, parent)
  if len(set(parent[1:])) == 1: return True
  return False

answer = []
queue = deque(graph)
for i in range(K):
  parent = [i for i in range(N+1)]
  total = 0
  for a, b, val in queue:
    if val == 0: continue
    if not findParent(a, b, parent):
      unionParent(a, b, parent)
      total += val
  
  queue.popleft()
  if confirmMST(parent):
    answer.append(total)
  else:
    answer.append(0)

print(*answer)