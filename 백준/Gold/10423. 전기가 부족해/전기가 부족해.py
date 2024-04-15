import sys
read = sys.stdin.readline

N, M, K = map(int, read().rstrip().split())
ARR_K = [*map(int, read().rstrip().split())]
ARR_M = [[*map(int, read().rstrip().split())] for _ in range(M)]

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

graph = sorted(ARR_M, key=lambda x: x[2])
parent = [i for i in range(N+1)]

# 발전소를 제일 작은 parent를 갖도록 한다.
for i, k in enumerate(ARR_K):
  parent[k] = 0

answer = 0
for a, b, val in graph:
  if not findParent(a, b, parent):
    unionParent(a, b, parent)
    answer += val

print(answer)
