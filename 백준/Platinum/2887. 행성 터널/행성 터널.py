import math
import sys
read = sys.stdin.readline

N = int(read().rstrip())
GRAPH = [[*map(int, read().rstrip().split())] for _ in range(N)]

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
graphX = []
graphY = []
graphZ = []

for i in range(N):
  x, y, z = GRAPH[i]
  graphX.append([x, i])
  graphY.append([y, i])
  graphZ.append([z, i])

graphX.sort()
graphY.sort()
graphZ.sort()

graph = []
for i in range(N-1):
  graph.append([graphX[i+1][0] - graphX[i][0], graphX[i][1], graphX[i+1][1]])
  graph.append([graphY[i+1][0] - graphY[i][0], graphY[i][1], graphY[i+1][1]])
  graph.append([graphZ[i+1][0] - graphZ[i][0], graphZ[i][1], graphZ[i+1][1]])

graph.sort()

answer = 0
for val, a, b in graph:
  if not findParent(a, b, parent):
    unionParent(a, b, parent)
    answer += val

print(answer)

