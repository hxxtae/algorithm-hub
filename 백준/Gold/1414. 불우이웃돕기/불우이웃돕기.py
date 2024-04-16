import sys
read = sys.stdin.readline

N = int(read().rstrip())
GRAPH = [read().rstrip() for _ in range(N)]

def changeCharToNum(char):
  if char.islower():
    return ord(char) - 96
  return (ord(char) - 64) + 26

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

parent = [i for i in range(N)]
graph = []
for r in range(N):
  for c in range(N):
    if GRAPH[r][c] == '0': continue
    graph.append((r, c, changeCharToNum(GRAPH[r][c])))
graph.sort(key=lambda x: x[2])

maxDist = 0
for a, b, val in graph:
  if not findParent(a, b, parent):
    unionParent(a, b, parent)
    continue
  maxDist += val

for i in range(N):
  getParent(i, parent)

# 모든 컴퓨터가 하나라도 연결되어 있지 않은 경우 확인
allConnect = all(parent[i] == 0 for i in range(N))

if len(parent) != 1 and not allConnect:
  print(-1)
else:
  print(maxDist)


