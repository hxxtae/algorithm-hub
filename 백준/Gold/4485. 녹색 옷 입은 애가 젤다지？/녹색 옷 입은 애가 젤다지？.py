from heapq import *
import sys
read = sys.stdin.readline

def findWay(y, x, way):
  X = [1, 0, -1, 0]
  Y = [0, 1, 0, -1]

  return [y + Y[way], x + X[way]]

def bfs(T):
  heap = [[MATRIX[0][0], 0, 0]] # [val, y, x]
  heapify(heap)
  distance = [[float('inf')] * N for _ in range(N)]
  distance[0][0] = MATRIX[0][0]
  
  while heap:
    val, y, x = heappop(heap)

    if distance[y][x] < val: continue

    for i in range(4):
      nextY, nextX = findWay(y, x, i)
      if nextY < 0 or nextX < 0 or nextY >= N or nextX >= N: continue
      newVal = val + MATRIX[nextY][nextX]
      if distance[nextY][nextX] > newVal:
        distance[nextY][nextX] = newVal
        heappush(heap, [newVal, nextY, nextX])
  
  print('Problem {}: {}'.format(T, distance[N - 1][N - 1]))

t = 1
while True:
  N = int(read().rstrip())
  if N == 0: break
  MATRIX = [[*map(int, read().rstrip().split())] for _ in range(N)]
  bfs(t)
  t += 1
  