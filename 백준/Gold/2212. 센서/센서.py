import sys
read = sys.stdin.readline

N = int(read().rstrip())
K = int(read().rstrip())
ARR = [*map(int, read().rstrip().split())]

if K >= N:
  print(0)
  exit()

ARR.sort()
distance = []

for i in range(1, N):
  distance.append(ARR[i] - ARR[i-1])
distance.sort()

for _ in range(K-1):
  distance.pop()

print(sum(distance))
