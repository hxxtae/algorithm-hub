import sys
read = sys.stdin.readline

N = int(read().rstrip())

INF = float('inf')
answer = INF
fiveCnt = N // 5
for i in range(fiveCnt + 1):
  cnt = i
  n = N - (i * 5)

  if n % 2 == 0:
    cnt += (n // 2)
    answer = min(answer, cnt)
  
if answer == INF:
  print(-1)
else:
  print(answer)