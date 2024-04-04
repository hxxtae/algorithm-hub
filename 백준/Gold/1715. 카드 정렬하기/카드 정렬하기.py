import sys
from heapq import *
read = sys.stdin.readline

N = int(read().rstrip())
ARR = [int(read().rstrip()) for _ in range(N)]

answer = []
heapify(ARR)
while len(ARR) > 1:
  sumNum = sum([heappop(ARR), heappop(ARR)])
  answer.append(sumNum)
  heappush(ARR, sumNum)

print(sum(answer))
