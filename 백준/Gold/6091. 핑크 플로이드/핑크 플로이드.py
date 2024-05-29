from heapq import *
import sys
read = sys.stdin.readline

N = int(read().rstrip())
GRAPH = [[*map(int, read().rstrip().split())] for _ in range(N-1)]

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

parent = [i for i in range(N+1)]
graph = []
for i, arr in enumerate(GRAPH):
  for j, dist in enumerate(arr):
    graph.append((dist, (i+1), (j+1)+(i+1)))

graph.sort()

answer = [[] for _ in range(N)]
for dist, a, b in graph:
  if not findParent(a, b, parent):
    unionParent(a, b, parent)
    answer[a-1].append(b)
    answer[b-1].append(a)

for arr in answer:
  print(len(arr), *sorted(arr))


