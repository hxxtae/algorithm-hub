from heapq import *
import sys
read = sys.stdin.readline

N, M, T, D = map(int, read().rstrip().split())
MATRIX = [read().rstrip() for _ in range(N)]

def findWay(y, x, way):
  X = [1, 0, -1, 0]
  Y = [0, 1, 0, -1]
  return [y + Y[way], x + X[way]]

def getHeight(c):
  num = ord(c)
  if c.isupper():
    return num  - 65
  return num - 71

def onDijkstra(startY, startX):
  times = [[float('inf')] * M for _ in range(N)]
  times[startY][startX] = 0
  heap = [[0, startY, startX]] # [time, y, x]
  heapify(heap)

  while heap:
    time, y, x = heappop(heap)
    nowHeight = getHeight(MATRIX[y][x])

    for i in range(4):
      nextY, nextX = findWay(y, x, i)
      if nextY < 0 or nextX < 0 or nextY >= N or nextX >= M: continue

      nextHeight = getHeight(MATRIX[nextY][nextX])
      nextTime = 0

      # 높이 비교
      if abs(nextHeight - nowHeight) > T: continue
      if nowHeight >= nextHeight:
        nextTime = time + 1
      else:
        nextTime = time + ((nextHeight - nowHeight) ** 2)
      
      # 시간 비교
      if times[nextY][nextX] <= nextTime: continue
      times[nextY][nextX] = nextTime
      heappush(heap, [nextTime, nextY, nextX])

  return times

arrives = onDijkstra(0, 0)
heights = []
heapify(heights)
for r in range(N):
  for c in range(M):
    if arrives[r][c] > D: continue
    heappush(heights, [-getHeight(MATRIX[r][c]), r, c]) # [height, y, x]

while heights:
  height, y, x = heappop(heights)
  reverse_arrives = onDijkstra(y, x)

  if arrives[y][x] + reverse_arrives[0][0] > D: continue
  print(-height)
  break
