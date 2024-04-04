import sys
from heapq import *
read = sys.stdin.readline

N = int(read().rstrip())
ARR = []
heapify(ARR)

for _ in range(N):
  for num in read().rstrip().split(' '):
    num = int(num)
    if len(ARR) < N:
      heappush(ARR, num)
    else:
      if ARR[0] < num:
        heappop(ARR)
        heappush(ARR, num)

print(ARR[0])