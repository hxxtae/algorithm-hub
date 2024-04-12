from itertools import combinations
import math
import sys
read = sys.stdin.readline

N = int(read().rstrip())
STARS = [[i+1, *map(float, read().rstrip().split())] for i in range(N)]

parent = [i for i in range(N+1)]

def distanceAandB(pos1, pos2):
  x1, y1 = pos1
  x2, y2 = pos2
  a = x1 - x2
  b = y1 - y2
  
  return round(math.sqrt((a * a) + (b * b)), 2)

graph = list(combinations(STARS, 2))
graph = list(map(lambda x: [x[0][0], x[1][0], distanceAandB(x[0][1:], x[1][1:])] , graph))
graph.sort(key=lambda x: x[2])

def getParent(x, parent):
  return x if x == parent[x] else getParent(parent[x], parent)

def unionParent(x, y, parent):
  a, b = [getParent(x, parent), getParent(y, parent)]
  if a > b: parent[a] = b
  else: parent[b] = a

def findParent(x, y, parent):
  a, b = [getParent(x, parent), getParent(y, parent)]
  if a == b: return True
  return False

answer = 0
for a, b, val in graph:
  if not findParent(a, b, parent):
    unionParent(a, b, parent)
    answer += val

print(answer)