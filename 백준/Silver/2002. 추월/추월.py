import sys
from collections import defaultdict
read = sys.stdin.readline

N = int(read().rstrip())
IN = [read().rstrip() for _ in range(N)]
OUT = [read().rstrip() for _ in range(N)]

scoreDict = dict()
for score, car in enumerate(IN):
  scoreDict[car] = score+1

cnt = 0
for i, car in enumerate(OUT):
  for j in range(i, N):
    behindCar = OUT[j]
    if scoreDict[car] > scoreDict[behindCar]:
      cnt += 1
      break

print(cnt)