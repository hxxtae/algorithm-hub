import sys
from collections import deque, defaultdict
read = sys.stdin.readline

N = int(read().rstrip())
K = int(read().rstrip())
KARR = [[*map(int, read().rstrip().split(' '))] for _ in range(K)]
L = int(read().rstrip())
LARR = [read().rstrip().split(' ') for _ in range(L)]

board = [[0] * N for _ in range(N)]
snakeWay = defaultdict(str)

for apY, apX in KARR:
  board[apY-1][apX-1] = 2

for time, move in LARR:
  snakeWay[time] = move

def nextWay(way, wayStr):
  direc = {"L": -1, "D": 1}
  way += direc[wayStr]
  if way == -1:
    way = 3
  if way == 4:
    way = 0
  
  return way

def findWay(y, x, way):
  X = [1, 0, -1, 0]
  Y = [0, 1, 0, -1]

  return [y + Y[way], x + X[way]]

def snakeGame(startY, startX):
  init = [startY, startX]
  deq = deque([init])
  board[startY][startX] = 1
  
  time = 0
  way = 0
  while True:
    y, x = deq[-1]    
    nextY, nextX = findWay(y, x, way)
    
    # 벽 판단
    if nextY < 0 or nextX < 0 or nextY >= N or nextX >= N: break
    # 자기 몸 닿는지 판단
    if board[nextY][nextX] == 1: break
    # 사과 판단(꼬리 여부 결정)
    if board[nextY][nextX] == 2:
      deq.append([nextY, nextX])
    else:
      deq.append([nextY, nextX])
      prevY, prevX = deq.popleft()
      board[prevY][prevX] = 0

    board[nextY][nextX] = 1

    # 다음 방향 판단
    time += 1
    if snakeWay[str(time)]:
      way = nextWay(way, snakeWay[str(time)])
  
  return time

answer = snakeGame(0, 0)
print(answer + 1)
