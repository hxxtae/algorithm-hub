from heapq import *
import sys
read = sys.stdin.readline

N = int(read().rstrip())
ARR = [int(read().rstrip()) for _ in range(N)]

heap = []
heapify(heap)
for num in ARR:
  if num == 0:
    if len(heap) == 0:
      print(0)
    else:
      print(heappop(heap))
    continue
  
  heappush(heap, num)
  