import sys
read = sys.stdin.readline

N = int(read().rstrip())
FIELD = [list(map(int, read().rstrip())) for _ in range(N)]

def findWay(y, x, way):
  X = [1, 0, -1, 0]
  Y = [0, 1, 0, -1]

  return [y + Y[way], x + X[way]]

def dfs(y, x, cnt):
  FIELD[y][x] = 0
  
  for i in range(4):
    nextY, nextX = findWay(y, x, i)
    if nextY < 0 or nextX < 0 or nextY >= N or nextX >= N: continue
    if not FIELD[nextY][nextX]: continue
    cnt = dfs(nextY, nextX, cnt + 1)
  
  return cnt

answer = []
for r in range(N):
  for c in range(N):
    if not FIELD[r][c]: continue
    FIELD[r][c] = 0
    cnt = dfs(r, c, 1)
    answer.append(cnt)

print(len(answer))
print("\n".join(map(str, sorted(answer))))