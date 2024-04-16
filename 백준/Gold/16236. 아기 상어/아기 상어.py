from collections import deque
from heapq import *
import sys
read = sys.stdin.readline

N = int(read().rstrip())
MATRIX = [[*map(int, read().rstrip().split())] for _ in range(N)]

# 초기 아기 상어 위치 찾기
for r in range(N):
  for c in range(N):
    if MATRIX[r][c] == 9:
      baby = [r, c]

# 상하좌우 이동
def findWay(y, x, way):
  X = [1, 0, -1, 0]
  Y = [0, 1, 0, -1]
  return [y + Y[way], x + X[way]]

# 가장 가까운 물고기들의 위치 탐색
def findFish(startY, startX, babySize):
  queue = deque([[startY, startX, 0]])
  visited = [[0] * N for _ in range(N)]
  visited[startY][startX] = 1
  MATRIX[startY][startX] = 0
  notFount = True

  while queue:
    y, x, cnt = queue.popleft()

    for i in range(4):
      nextY, nextX = findWay(y, x, i)
      if nextY < 0 or nextX < 0 or nextY >= N or nextX >= N: continue
      if visited[nextY][nextX]: continue
      if MATRIX[nextY][nextX] > babySize: continue
      visited[nextY][nextX] = cnt + 1
      queue.append([nextY, nextX, cnt + 1])
      notFount = False
  
  if notFount:
    return []
  return visited

# 가까운 물고기 먹으로 이동
def moveBabyToFish():
  # init
  babyY, babyX = baby
  babySize = 2
  time = 0
  eat = 0

  while True:
    visited = findFish(babyY, babyX, babySize)
    if not visited:
      return time
    
    # 물고기 찾기
    heap = []
    heapify(heap)
    for r in range(N):
      for c in range(N):
        if (MATRIX[r][c] != 0) and (MATRIX[r][c] < babySize and visited[r][c]):
          heappush(heap, [visited[r][c], r, c]) # 거리, Y좌표, X좌표

    if not len(heap):
      return time

    # print(heap[0])

    dist, y, x = heappop(heap)
    time += dist
    babyY, babyX = y, x
    eat += 1
    MATRIX[y][x] = 0

    if eat == babySize:
      babySize += 1
      eat = 0

print(moveBabyToFish())
