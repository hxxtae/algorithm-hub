from collections import deque
import sys
read = sys.stdin.readline

M, N, H = map(int, read().rstrip().split(' '))
BOXS = [[[*map(int, read().rstrip().split(' '))] for _ in range(N)] for _ in range(H)]

queue = deque()

def findWay(z, y, x, way):
  X = [1, 0, -1, 0, 0, 0]
  Y = [0, 1, 0, -1, 0, 0]
  Z = [0, 0, 0, 0, 1, -1]

  return [z + Z[way], y + Y[way], x + X[way]]

def bfs():
  while queue:
    z, y, x = queue.popleft()
    
    for i in range(6):
      nextZ, nextY, nextX = findWay(z, y, x, i)
      if nextZ < 0 or nextY < 0 or nextX < 0 or nextZ >= H or nextY >= N or nextX >= M: continue
      if BOXS[nextZ][nextY][nextX] != 0: continue
      BOXS[nextZ][nextY][nextX] = BOXS[z][y][x] + 1
      queue.append([nextZ, nextY, nextX])


for z in range(H):
  for r in range(N):
    for c in range(M):
      if BOXS[z][r][c] == 1:
        queue.append([z, r, c])

bfs()

day = 0
for z in range(H):
  for r in range(N):
    for c in range(M):
      if BOXS[z][r][c] == 0:
        print(-1)
        exit(0)
      day = max(day, BOXS[z][r][c])

print(day - 1)