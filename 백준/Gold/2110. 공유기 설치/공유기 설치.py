import sys
read = sys.stdin.readline

N, M = map(int, read().rstrip().split(' '))
ARR = [*map(int, [read().rstrip() for _ in range(N)])]

ARR.sort()
minDis = 1
maxDis = max(ARR)
halfDis = 0

while minDis <= maxDis:
  halfDis = (minDis + maxDis) // 2
  cnt = 1
  prevHome = ARR[0]

  for num in ARR[1:]:
    if (num - prevHome) >= halfDis:
      cnt += 1
      prevHome = num
  
  if cnt >= M:
    minDis = halfDis + 1
  
  if cnt < M:
    maxDis = halfDis - 1

print(maxDis)