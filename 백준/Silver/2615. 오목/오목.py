import sys
read = sys.stdin.readline

BOARD = ["".join(read().rstrip().split(' ')) for _ in range(19)]

# 모든방향
def findWay(y, x, way):
  X = [1, 1, 0, -1, -1, -1, 0, 1]
  Y = [0, 1, 1, 1, 0, -1, -1, -1]

  return [y + Y[way], x + X[way]]

# 탐색
def dfs(y, x, way, kind, arr):
  if len(arr) >= 6:
    return arr
  
  nextY, nextX = findWay(y, x, way)
  if nextY < 0 or nextX < 0 or nextY >= 19 or nextX >= 19: return arr
  if BOARD[nextY][nextX] == '0': return arr
  if BOARD[nextY][nextX] not in kind: return arr
  arr.append([nextY, nextX])
  arr = dfs(nextY, nextX, way, kind, arr)

  return arr

# 오목 찾기
def findAnswer():
  answer = []
  for r in range(19):
    for c in range(19):
      if BOARD[r][c] == '0': continue
      kind = BOARD[r][c]
      for i in range(4):
        arr = dfs(r, c, i, kind, [[r, c]])
        arr = dfs(r, c, i+4, kind, arr)
        if len(arr) < 5: continue
        if len(arr) >= 6: continue
        
        answer.append(kind)
        arr.sort(key=lambda x: (x[1], x[0]))
        answer.append(" ".join(map(lambda x: str(x + 1), arr[0])))
        return "\n".join(answer)

  return 0

# 실행
print(findAnswer())