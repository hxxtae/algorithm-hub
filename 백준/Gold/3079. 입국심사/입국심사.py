import sys
read = sys.stdin.readline

N, M = [*map(int, read().rstrip().split(' '))]
ARR = [int(read().rstrip()) for _ in range(N)]
timeMin = min(ARR)
timeMax = max(ARR) * M
timeHalf = 0

while timeMin <= timeMax:
  timeHalf = (timeMin + timeMax) // 2
  cnt = 0
  
  for num in ARR:
    if num <= timeHalf:
      cnt += (timeHalf // num)
  
  if cnt >= M:
    timeMax = timeHalf - 1
  
  if cnt < M:
    timeMin = timeHalf + 1

print(timeMin)