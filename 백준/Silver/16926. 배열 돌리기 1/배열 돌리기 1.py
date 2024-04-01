import sys
read = sys.stdin.readline

N, M, R = map(int, read().rstrip().split(' '))
ARR = [read().rstrip().split(' ') for _ in range(N)]

cycleArrCnt = int(min(N, M) / 2) # 돌려야 하는 배열들의 개수
cycleArrStart = [[i, i] for i in range(cycleArrCnt)] # 돌려야 하는 배열들의 시작점
cycleArrMove = [[(N-1)-(i*2), (M-1)-(i*2), (N-1)-(i*2), (M-1)-(i*2)] for i in range(cycleArrCnt)] # 돌려야 하는 배열들의 y,x 방향 이동 길이

def moveYX(y, x, move, way, prev, curr):
  X = [0, 1, 0, -1]
  Y = [1, 0, -1, 0]
  for _ in range(move):
    y, x = [y + Y[way], x + X[way]]
    curr = ARR[y][x]
    ARR[y][x] = prev
    prev = curr
  
  return [y, x, prev, curr]

for i in range(cycleArrCnt):
  totalMove = R % sum(cycleArrMove[i])
  for _ in range(totalMove):

    y, x = cycleArrStart[i]
    prev = ARR[y][x]
    curr = ''

    for way in range(4):
      move = cycleArrMove[i][way]
      y, x, prev, curr = moveYX(y, x, move, way, prev, curr)

print("\n".join(map(lambda x: " ".join(x), ARR)))