import sys
read = sys.stdin.readline

N = int(read().rstrip())
ARR = [[*map(int, read().rstrip().split())] for _ in range(N)]

arr = sorted(ARR, key=lambda x: (x[0], x[1]))
currTime = 0
for a, b in arr:
  if currTime < a:
    currTime = (a + b)
  else:
    currTime += b

print(currTime)