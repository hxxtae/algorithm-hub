from heapq import *
import sys
read = sys.stdin.readline

N = int(read().rstrip())
MATRIX = [read().rstrip() for _ in range(N)]

def findWay(y, x, way):
  X = [1, 0, -1, 0]
  Y = [0, 1, 0, -1]

  return [y + Y[way], x + X[way]]

def bfs():
  heap = [[0, 0, 0]] # [count, y, x]
  heapify(heap)
  visited = [[0] * N for _ in range(N)]
  visited[0][0] = 1

  while heap:
    count, y, x = heappop(heap)
    
    if y == (N-1) and x == (N-1):
      return count

    for i in range(4):
      nextY, nextX = findWay(y, x, i)
      if nextY < 0 or nextX < 0 or nextY >= N or nextX >= N: continue
      if visited[nextY][nextX]: continue
      visited[nextY][nextX] = 1

      if MATRIX[nextY][nextX] in '1': # 흰 방
        heappush(heap, [count, nextY, nextX])
      else: # 검은 방
        heappush(heap, [count + 1, nextY, nextX])
  
  return 0

print(bfs())