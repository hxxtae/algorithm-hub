import sys
read = sys.stdin.readline

T = int(read().rstrip())
answer = []

# 상하좌우 탐색
def findWay(y, x, way):
  X = [1, 0, -1, 0]
  Y = [0, 1, 0, -1]

  return [y + Y[way], x + X[way]]

# DFS
# -> 런타임 에러 (RecursionError): Python이 정한 최대 재귀 깊이보다 재귀의 깊이가 더 깊어질 때입니다.
def dfs(y, x, n, m, field):
  field[y][x] = 0
  
  for i in range(4):
    nextY, nextX = findWay(y, x, i)
    if nextY < 0 or nextX < 0 or nextY >= n or nextX >= m: continue
    if not field[nextY][nextX]: continue
    dfs(nextY, nextX, n, m, field)

# BFS
def bfs(startY, startX, n, m, field):
  queue = [[startY, startX]]
  field[startY][startX] = 0

  while queue:
    y, x = queue.pop(0)

    for i in range(4):
      nextY, nextX = findWay(y, x, i)
      if nextY < 0 or nextX < 0 or nextY >= n or nextX >= m: continue
      if not field[nextY][nextX]: continue
      field[nextY][nextX] = 0
      queue.append([nextY, nextX])

# 실행
for _ in range(T):
  M, N, K = map(int, read().rstrip().split(' '))
  FIELD = [[0] * M for _ in range(N)]
  for _ in range(K):
    x, y = map(int, read().rstrip().split(' '))
    FIELD[y][x] = 1
  
  cnt = 0
  for r in range(N):
    for c in range(M):
      if not FIELD[r][c]: continue
      FIELD[r][c] = 0
      # dfs(r, c, N, M, FIELD)
      bfs(r, c, N, M, FIELD)
      cnt += 1
  
  answer.append(str(cnt))

print("\n".join(answer))