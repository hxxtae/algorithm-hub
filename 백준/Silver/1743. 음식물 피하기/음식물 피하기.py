from collections import deque
import sys
read = sys.stdin.readline

N, M, K = [*map(int, read().rstrip().split())]
GRAPH = [[*map(int, read().rstrip().split())] for _ in range(K)]

matrix = [["."] * M for _ in range(N)]
for y, x in GRAPH:
  matrix[y-1][x-1] = '#'

def findWay(y, x, way):
  X = [1, 0, -1, 0]
  Y = [0, 1, 0, -1]

  return [y + Y[way], x + X[way]]

def bfs(startY, startX):
  queue = deque([[startY, startX]])
  matrix[startY][startX] = '.'
  cnt = 0

  while queue:
    y, x = queue.popleft()
    cnt += 1

    for i in range(4):
      nextY, nextX = findWay(y, x, i)
      if nextY < 0 or nextX < 0 or nextY >= N or nextX >= M: continue
      if matrix[nextY][nextX] == '.': continue
      matrix[nextY][nextX] = '.'
      queue.append([nextY, nextX])

  return cnt

answer = 0
for r in range(N):
  for c in range(M):
    if matrix[r][c] == '#':
      answer = max(answer, bfs(r, c))

print(answer)