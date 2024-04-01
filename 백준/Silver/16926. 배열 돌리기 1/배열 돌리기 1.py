import sys
from collections import deque
read = sys.stdin.readline

N, M, R = map(int, read().rstrip().split(' '))
ARR = [read().rstrip().split(' ') for _ in range(N)]

answer = [[0] * M for _ in range(N)]
cycleArrCnt = min(N, M) // 2
cycleArrMove = [((N-1)-(i*2)+(M-1)-(i*2))*2 for i in range(cycleArrCnt)]
dq = deque()

for i in range(cycleArrCnt):
  dq.clear()
  dq.extend(ARR[i][i:M-i])
  dq.extend([r[M-1-i] for r in ARR[i+1:N-1-i]])
  dq.extend(ARR[N-1-i][i:M-i][::-1])
  dq.extend([r[i] for r in ARR[i+1:N-1-i]][::-1])

  moveR = R % cycleArrMove[i]
  dq.rotate(-moveR)

  for j in range(i, M-i):
    answer[i][j] = dq.popleft()
  for j in range(i+1, N-1-i):
    answer[j][M-1-i] = dq.popleft()
  for j in range(M-1-i, i-1, -1):
    answer[N-1-i][j] = dq.popleft()  
  for j in range(N-2-i, i, -1):
    answer[j][i] = dq.popleft()  

print("\n".join(map(lambda x: " ".join(x), answer)))
