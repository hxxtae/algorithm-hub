from collections import deque
import sys
read = sys.stdin.readline

R, C = map(int, read().rstrip().split())
BOARD = [read().rstrip() for _ in range(R)]

queueWater = deque()
queueS = deque()
visitedWater = [[0] * C for _ in range(R)]
visitedS = [[0] * C for _ in range(R)]

def findWay(y, x, way):
  X = [1, 0, -1, 0]
  Y = [0, 1, 0, -1]

  return [y + Y[way], x + X[way]]

def bfs(queue, kind):
  while queue:
    y, x, cnt = queue.popleft()

    for i in range(4):
      nextY, nextX = findWay(y, x, i)
      if nextY < 0 or nextX < 0 or nextY >= R or nextX >= C: continue
      # 물이 차오르는 시뮬레이션(탐색)
      if kind == "*":
        if BOARD[nextY][nextX] != "." or visitedWater[nextY][nextX] != 0: continue
        visitedWater[nextY][nextX] = cnt + 1
      # 고슴도치가 이동하는 시뮬레이션(탐색)
      if kind == "S":
        if BOARD[nextY][nextX] == 'D': return cnt + 1
        if BOARD[nextY][nextX] != "." or visitedS[nextY][nextX]: continue
        if visitedWater[nextY][nextX] != 0 and visitedWater[nextY][nextX] <= (cnt+1): continue
        visitedS[nextY][nextX] = cnt + 1
      queue.append([nextY, nextX, cnt + 1])

for r in range(R):
  for c in range(C):
    if BOARD[r][c] == '*':
      queueWater.append([r, c, 1])
      visitedWater[r][c] = 1
    if BOARD[r][c] == 'S':
      queueS.append([r, c, 1])
      visitedS[r][c] = 1

bfs(queueWater, '*')
answer = bfs(queueS, 'S')

if answer:
  print(answer - 1)
else:
  print('KAKTUS')