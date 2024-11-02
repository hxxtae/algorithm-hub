import sys
read = sys.stdin.readline

A, B = map(int, read().rstrip().split())
N = int(read().rstrip())
nArr = [int(read().rstrip()) for _ in range(N)]

minDist = abs(A - B)
onChange = False
for pos in nArr:
  dist = abs(B - pos)
  if minDist > dist:
    onChange = True
    minDist = dist

if onChange:
  print(minDist + 1)
else:
  print(minDist)