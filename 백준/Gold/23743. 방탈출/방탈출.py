import sys
read = sys.stdin.readline

N, M = map(int, read().rstrip().split())
graph = [[*map(int, read().rstrip().split())] for _ in range(M)]
EXIT_LIST = [*map(int, read().rstrip().split())]

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

for i in range(N):
  graph.append([0, i+1, EXIT_LIST[i]])

graph.sort(key=lambda x: x[2])

parent = [i for i in range(N+1)]
answer = 0
for a, b, dist in graph:
  if not findParent(a, b, parent):
    unionParent(a, b, parent)
    answer += dist

print(answer)