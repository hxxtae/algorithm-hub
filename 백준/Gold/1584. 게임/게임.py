from heapq import *
import sys
read = sys.stdin.readline

N = int(read().rstrip())
N_LIST = [[*map(int, read().rstrip().split())] for _ in range(N)]
M = int(read().rstrip())
M_LIST = [[*map(int, read().rstrip().split())] for _ in range(M)]

# 위험 구역 범위 지정 (왼쪽상단 모서리 ~ 오른쪽하단 모서리, 즉 사각형 형태의 범위 지정)
dangers = []
for x1, y1, x2, y2 in N_LIST:
  if x1 > x2:
    x1, x2 = x2, x1
  if y1 > y2:
    y1, y2 = y2, y1
  dangers.append([x1, y1, x2, y2])

# 죽음 구역 범위 지정 (왼쪽상단 모서리 ~ 오른쪽하단 모서리, 즉 사각형 형태의 범위 지정)
deaths = []
for x1, y1, x2, y2 in M_LIST:
  if x1 > x2:
    x1, x2 = x2, x1
  if y1 > y2:
    y1, y2 = y2, y1
  deaths.append([x1, y1, x2, y2])

def findWay(x, y, way):
  X = [1, 0, -1, 0]
  Y = [0, 1, 0, -1]
  return [x + X[way], y + Y[way]]

def onDijkstra():
  # Set Distance
  distance = [[float('inf')] * 501 for _ in range(501)]
  distance[0][0] = 0
  
  # BFS
  heap = [[0, 0, 0]] # dist, x, y
  heapify(heap)
  while heap:
    dist, x, y = heappop(heap)

    if distance[y][x] < dist: continue

    for i in range(4):
      nextX, nextY = findWay(x, y, i)
      if nextX < 0 or nextY < 0 or nextX >= 501 or nextY >= 501: continue

      flag = False
      for x1, y1, x2, y2 in deaths:
        if x1 <= nextX <= x2 and y1 <= nextY <= y2:
          flag = True
          break
      if flag: continue

      addLife = 0
      for x1, y1, x2, y2 in dangers:
        if x1 <= nextX <= x2 and y1 <= nextY <= y2:
          addLife += 1
          break
      
      new_dist = dist + addLife
      if new_dist < distance[nextY][nextX]:
        distance[nextY][nextX] = new_dist
        heappush(heap, [new_dist, nextX, nextY])
  
  return distance[500][500]

answer = onDijkstra()
if answer == float('inf'):
  print(-1)
else:
  print(answer)
