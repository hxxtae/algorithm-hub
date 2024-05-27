from collections import deque
import sys
read = sys.stdin.readline

N, M = map(int, read().rstrip().split())
MATRIX = [[*read().rstrip()] for _ in range(N)]

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

def findWay(y, x, way):
  X = [1, 0, -1, 0]
  Y = [0, 1, 0, -1]

  return [y + Y[way], x + X[way]]

def bfs(startY, startX, arr):
  visited = [([0] * N) for _ in range(N)]
  visited[startY][startX] = 1
  queue = deque([[startY, startX, 0]]) # [y, x, dist]
  # aNode = int(str(startY)+str(startX))
  startNode = nodes[startY][startX]

  while queue:
    y, x, dist = queue.popleft()
    
    for i in range(4):
      nextY, nextX = findWay(y, x, i)
      if MATRIX[nextY][nextX] == "1": continue
      if visited[nextY][nextX]: continue
      visited[nextY][nextX] = 1
      queue.append([nextY, nextX, dist + 1])
      if MATRIX[nextY][nextX] in "S" or MATRIX[nextY][nextX] in "K":
        # bNode = int(str(nextY)+str(nextX))
        endNode = nodes[nextY][nextX]
        arr.append([dist + 1, startNode, endNode])

nodes = [[0]*N for _ in range(N)] # 좌표의 S, K를 노드 번호로 지정
parent = [i for i in range(M+1)]
cnt = 0
for r in range(N):
  for c in range(N):
    if MATRIX[r][c] in "S" or MATRIX[r][c] in "K":
      nodes[r][c] = cnt
      cnt += 1

arr = []
for r in range(1, N-1):
  for c in range(1, N-1):
    if MATRIX[r][c] in "S" or MATRIX[r][c] in "K":
      bfs(r, c, arr)

arr.sort()

answer = 0
for dist, a, b in arr:
  if not findParent(a, b, parent):
    unionParent(a, b, parent)
    answer += dist

if all(i == 0 for i in parent):
  print(answer)
else:
  print(-1)