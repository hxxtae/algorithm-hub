from collections import deque
import sys
read = sys.stdin.readline

N = int(read().rstrip())
GRAPH = [read().rstrip() for _ in range(N)]

visited = [[0] * N for _ in range(N)]

def findWay(y, x, way):
  X = [1, 0, -1, 0]
  Y = [0, 1, 0, -1]

  return [y + Y[way], x + X[way]]

def redGreenBlind(color):
  if color == 'B': return 'B'
  return ['R', 'G']

def bfs(startY, startX, startColor, kind):
  queue = deque([[startY, startX, startColor]])
  visited[startY][startX] = kind

  while queue:
    [y, x, color] = queue.popleft()

    for i in range(4):
      nextY, nextX = findWay(y, x, i)
      if nextY < 0 or nextX < 0 or nextY >= N or nextX >= N: continue
      if kind == 2 and (GRAPH[nextY][nextX] not in redGreenBlind(color)): continue
      if kind == 1 and (GRAPH[nextY][nextX] not in color): continue
      if visited[nextY][nextX] == kind: continue
      visited[nextY][nextX] = kind
      queue.append([nextY, nextX, GRAPH[nextY][nextX]])

answer = []
cnt = 0
for kind in range(1, 3): # 1: 일반 / 2: 적록색약
  for r in range(N):
    for c in range(N):
      if visited[r][c] == kind: continue
      bfs(r, c, GRAPH[r][c], kind)
      cnt += 1
  answer.append(cnt)
  cnt = 0

print(*answer)