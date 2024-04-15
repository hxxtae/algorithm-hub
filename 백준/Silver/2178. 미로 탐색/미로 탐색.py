from collections import deque
import sys
read = sys.stdin.readline

N, M = map(int, read().rstrip().split())
BOARD = [read().rstrip() for _ in range(N)]

def findWay(y, x, way):
  X = [1, 0, -1, 0]
  Y = [0, 1, 0, -1]

  return [y + Y[way], x + X[way]]

def bfs():
  queue = deque([[0, 0, 1]])
  visited[0][0] = 1
  
  while queue:
    y, x, cnt = queue.popleft()

    if y == N-1 and x == M-1:
      return cnt

    for i in range(4):
      nextY, nextX = findWay(y, x, i)
      if nextY < 0 or nextX < 0 or nextY >= N or nextX >= M: continue
      if '0' in BOARD[nextY][nextX]: continue
      if visited[nextY][nextX]: continue
      visited[nextY][nextX] = 1
      queue.append([nextY, nextX, cnt+1])
    
visited = [[0] * M for _ in range(N)]
print(bfs())
