import sys
read = sys.stdin.readline

N = int(read().rstrip())
ARR = [*map(int, read().rstrip().split(' '))]

ARR.sort()
total = float('inf')
answer = [0, 0, 0]

for i in range(N):
  start = i + 1
  end = N - 1

  while start < end:
    sumOne = ARR[i] + ARR[start] + ARR[end]
    if abs(sumOne) < total:
      total = abs(sumOne)
      answer = [ARR[i], ARR[start], ARR[end]]

    if total == 0:
      break

    if sumOne < 0:
      start += 1
    
    if sumOne > 0:
      end -= 1

print(*sorted(answer))