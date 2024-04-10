from heapq import *
import sys
read = sys.stdin.readline

N = int(read().rstrip())
ARR_N = [*map(int, read().rstrip().split())]
M = int(read().rstrip())
ARR_M = [*map(int, read().rstrip().split())]

ARR_N.sort()
answer = [0] * M

for i, num in enumerate(ARR_M):
  start = 0
  end = N - 1

  while start <= end:
    half = (start + end) // 2
    if num == ARR_N[half]:
      answer[i] = 1
      break
    
    if num > ARR_N[half]:
      start = half + 1
    else:
      end = half - 1

print("\n".join(map(str, answer)))
