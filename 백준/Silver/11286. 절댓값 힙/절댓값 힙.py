import sys
from heapq import *
read = sys.stdin.readline

N = int(read().rstrip())
ARR = []
heapify(ARR)

for _ in range(N):
  num = int(read().rstrip())
  numArr = [abs(num), num]
  if num == 0:
    if len(ARR) == 0:
      print(0)
      continue

    print(heappop(ARR)[1])
    continue

  heappush(ARR, numArr)
