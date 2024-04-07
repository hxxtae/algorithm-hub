from heapq import *
import sys
read = sys.stdin.readline

N, K = map(int, read().rstrip().split(' '))
JEWELS = [[*map(int, read().rstrip().split(' '))] for _ in range(N)]
BAGS = [int(read().rstrip()) for _ in range(K)]

JEWELS.sort()
BAGS.sort()
ARR = []
answer = 0

for bag in BAGS:
  while JEWELS and JEWELS[0][0] <= bag:
    heappush(ARR, -JEWELS[0][1])
    heappop(JEWELS)
  if ARR:
    answer -= heappop(ARR)

print(answer)
