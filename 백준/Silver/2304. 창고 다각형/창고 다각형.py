import sys
read = sys.stdin.readline

N = int(read().rstrip())
ARR = [[*map(int, read().rstrip().split(' '))] for _ in range(N)]

ARR = sorted(ARR, key=lambda x: x[0])
answer = 0
maxY = 0
maxYofX = 0
maxX = 0

for x, y in ARR:
  if y > maxY:
    maxY = y
    maxYofX = x
  if x > maxX:
    maxX = x

heightes = [0] * (maxX+1)

for x, y in ARR:
  heightes[x] = y

for i in range(1, maxYofX):
  if heightes[i-1] > heightes[i]:
    heightes[i] = heightes[i-1]

for i in range(maxX, maxYofX, -1):
  if heightes[i-1] < heightes[i]:
    heightes[i-1] = heightes[i]

print(sum(heightes))