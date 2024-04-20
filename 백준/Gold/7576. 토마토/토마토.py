from collections import deque
import sys
read = sys.stdin.readline

M, N = map(int, read().rstrip().split())
BOARD = [[*map(int, read().rstrip().split())] for _ in range(N)]

def findWay(y, x, way):
  X = [1, 0, -1, 0]
  Y = [0, 1, 0, -1]

  return [y + Y[way], x + X[way]]

def bfs():
  answer = 0
  while queue:
    y, x, cnt = queue.popleft()

    answer = max(answer, cnt)
    
    for i in range(4):
      nextY, nextX = findWay(y, x, i)
      if nextY < 0 or nextX < 0 or nextY >= N or nextX >= M: continue
      if BOARD[nextY][nextX] != 0: continue
      BOARD[nextY][nextX] = 1
      queue.append([nextY, nextX, cnt + 1])
  
  return answer

queue = deque([])
for r in range(N):
  for c in range(M):
    if BOARD[r][c] == 1:
      queue.append([r, c, 0])

answer = bfs()
for r in range(N):
  for c in range(M):
    if BOARD[r][c] == 0:
      print(-1)
      exit()
print(answer)