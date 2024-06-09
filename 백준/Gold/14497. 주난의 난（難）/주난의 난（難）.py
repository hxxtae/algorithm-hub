from heapq import *
import sys
read = sys.stdin.readline

N, M = map(int, read().rstrip().split())
OWNER_Y, OWNER_X, TARGET_Y, TARGET_X = map(int, read().rstrip().split())
GRAPH = [read().rstrip() for _ in range(N)]

def findWay(y, x, way):
  X = [1, 0, -1, 0]
  Y = [0, 1, 0, -1]
  return [y + Y[way], x + X[way]]

def bfs(startY, startX, endY, endX):
  heap = [[0, startY, startX]]
  heapify(heap)
  visited = [[0]*M for _ in range(N)]
  visited[startY][startX] = 1
  answer = float('inf')

  while heap:
    cnt, y, x = heappop(heap)

    if y == endY and x == endX:
      answer = min(answer, cnt)
    
    for i in range(4):
      nextY, nextX = findWay(y, x, i)
      if nextY < 0 or nextX < 0 or nextY >= N or nextX >= M: continue
      if visited[nextY][nextX]: continue

      if GRAPH[nextY][nextX] in "#":
        heappush(heap, [cnt + 1, nextY, nextX])
        continue

      if GRAPH[nextY][nextX] in "1":
        heappush(heap, [cnt + 1, nextY, nextX])
      elif GRAPH[nextY][nextX] in "0":
        heappush(heap, [cnt, nextY, nextX])
      visited[nextY][nextX] = 1
  
  return answer

print(bfs(OWNER_Y-1, OWNER_X-1, TARGET_Y-1, TARGET_X-1))