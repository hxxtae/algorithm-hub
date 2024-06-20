from heapq import *
import sys
read = sys.stdin.readline

N, M = map(int, read().rstrip().split())
MATRIX = [[*read().rstrip()] for _ in range(N)]

def findWay(y, x, way):
  X = [1, 0, -1, 0]
  Y = [0, 1, 0, -1]
  return [y + Y[way], x + X[way]]

# 시작점 찾기
# 도착점 찾기
# 쓰레기가 인접한 주변을 '*'로 변경
sy, sx = 0, 0
ey, ex = 0, 0
for r in range(N):
  for c in range(M):
    item = MATRIX[r][c]
    if item == "g":
      for i in range(4):
        nextY, nextX = findWay(r, c, i)
        if nextY < 0 or nextX < 0 or nextY >= N or nextX >= M: continue
        if MATRIX[nextY][nextX] != '.': continue
        MATRIX[nextY][nextX] = "*"
    elif item == "S":
      sy, sx = r, c
    elif item == "F":
      ey, ex = r, c

visited = [[0]*M for _ in range(N)]
visited[sy][sx] = 1
heap = [[0, 0, sy, sx]] # [쓰래기 지난 횟수, 쓰레기 주변을 지난 횟수, y, x]
heapify(heap)
while heap:
  t_cnt, r_cnt, y, x = heappop(heap)

  for i in range(4):
    nextY, nextX = findWay(y, x, i)
    if nextY < 0 or nextX < 0 or nextY >= N or nextX >= M: continue
    if visited[nextY][nextX]: continue
    visited[nextY][nextX] = 1

    if MATRIX[nextY][nextX] == ".":
      heappush(heap, [t_cnt, r_cnt, nextY, nextX])
    elif MATRIX[nextY][nextX] == "*":
      heappush(heap, [t_cnt, r_cnt + 1, nextY, nextX])
    elif MATRIX[nextY][nextX] == "g":
      heappush(heap, [t_cnt + 1, r_cnt, nextY, nextX])
    else:
      print(t_cnt, r_cnt)
      exit(0)
