import sys
from heapq import *
read = sys.stdin.readline

N = int(read().rstrip())
ARR = [*map(int, [read().rstrip() for _ in range(N)])]

ARR.sort(reverse=True)
setObj = set()

for i in range(N):
  for j in range(N):
    setObj.add(ARR[i] + ARR[j])

loopEnd = False
for i in range(N):
  for j in range(N):
    if (ARR[i] - ARR[j]) in setObj:
      print(ARR[i])
      loopEnd = True
    if loopEnd: break
  if loopEnd: break
