from collections import deque
import sys
read = sys.stdin.readline

N, M = [*map(int, read().rstrip().split())]
MATRIX = [[*map(int, read().rstrip().split())] for _ in range(N)]

def findWay(y, x, way):
  X = [1, 0, -1, 0]
  Y = [0, 1, 0, -1]

  return [y + Y[way], x + X[way]]

def bfs(startY, startX):
  queue = deque([[startY, startX]])
  MATRIX[startY][startX] = 0
  cnt = 0

  while queue:
    y, x = queue.popleft()

    cnt += 1
    for i in range(4):
      nextY, nextX = findWay(y, x, i)
      if nextY < 0 or nextX < 0 or nextY >= N or nextX >= M: continue
      if not MATRIX[nextY][nextX]: continue
      MATRIX[nextY][nextX] = 0
      queue.append([nextY, nextX])
  
  return cnt

maxSize = 0
count = 0
for r in range(N):
  for c in range(M):
    if MATRIX[r][c] == 1:
      maxSize = max(maxSize, bfs(r, c))
      count += 1

print(count)
print(maxSize)
