import sys
read = sys.stdin.readline

N = int(read().rstrip())
ARR_N = [*map(int, read().rstrip().split())]
M = int(read().rstrip())
ARR_M = [*map(int, read().rstrip().split())]

ARR_N.sort()
answer = []

for num in ARR_M:
  start = 0
  end = N - 1
  matche = False

  while start <= end:
    half = (start + end) // 2
    target = ARR_N[half]
    
    if num == target:
      answer.append(1)
      matche = True
      break
    
    if target < num:
      start = half + 1
    if target > num:
      end = half - 1
  
  if not matche:
    answer.append(0)

print(*answer)

