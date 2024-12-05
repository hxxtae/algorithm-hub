from heapq import *
import sys
read = sys.stdin.readline

N = int(read().rstrip())
ARR = list(map(int, read().rstrip().split()))

answer = 0
heap = [-num for num in ARR]
heapify(heap)
while len(heap):
  if len(heap) > 1:
    a = -(heappop(heap) + 1)
    b = -(heappop(heap) + 1)
    if a > 0: heappush(heap, -a)
    if b > 0: heappush(heap, -b)
  else:
    a = -(heappop(heap) + 1)
    if a > 0: heappush(heap, -a)
  
  answer += 1

if answer > 1440:
  print(-1)
else:
  print(answer)
