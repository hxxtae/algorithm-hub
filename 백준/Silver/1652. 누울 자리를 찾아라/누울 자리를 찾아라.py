import sys
read = sys.stdin.readline

N = int(read().rstrip())
ROOM = [read().rstrip() for _ in range(N)]

rowSpot = ROOM # 가로로 보는 자리들
colSpot = ["".join((ROOM[c][r] for c in range(N))) for r in range(N)] # 세로로 보는 자리들

answer = [0, 0] # 가로, 세로
for i in range(N):
  rCnt = 0
  cCnt = 0
  for j in range(N):
    r = rowSpot[i][j]
    c = colSpot[i][j]

    if r == 'X':
      if rCnt >= 2:
        answer[0] += 1
      rCnt = 0
    
    if c == 'X':
      if cCnt >= 2:
        answer[1] += 1
      cCnt = 0

    if r == '.':
      rCnt += 1
    
    if c == '.':
      cCnt += 1
  
  if rCnt >= 2:
    answer[0] += 1
  if cCnt >= 2:
    answer[1] += 1
    
print(*answer)