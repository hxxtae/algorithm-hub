from collections import deque
import sys
read = sys.stdin.readline

def findWay(y, x, way):
  X = [2, 2, 1, -1, -2, -2, -1, 1]
  Y = [-1, 1, 2, 2, 1, -1, -2, -2]

  return [y + Y[way], x + X[way]]

def bfs(startY, startX, endY, endX, length):
  if startY == endY and startX == endX:
    return 0
  
  matrix = [[0] * length for _ in range(length)]
  queue = deque([[startY, startX, 0]])
  matrix[startY][startX] = 1
  cnt = 0

  while queue:
    y, x, order = queue.popleft()
    if y == endY and x == endX:
      cnt = order
      break

    for i in range(8):
      nextY, nextX = findWay(y, x, i)
      if nextY < 0 or nextX < 0 or nextY >= length or nextX >= length: continue
      if matrix[nextY][nextX] == 1: continue
      matrix[nextY][nextX] = 1
      queue.append([nextY, nextX, order + 1])
  
  return cnt

T = int(read().rstrip())
for _ in range(T):
  I = int(read().rstrip())
  SY, SX = map(int, read().rstrip().split(' '))
  EY, EX = map(int, read().rstrip().split(' '))
  print(bfs(SY, SX, EY, EX, I))
