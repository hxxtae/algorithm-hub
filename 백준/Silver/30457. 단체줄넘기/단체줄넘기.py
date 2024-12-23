import sys
read = sys.stdin.readline

N = int(read().rstrip())
ARR = list(map(int, read().rstrip().split()))

ARR.sort()
A = []
B = []

answer = 0
i = 0
while True:
  if len(ARR) == i:
    break
  A.append(ARR[i])
  i += 1

  if len(ARR) == i:
    break
  B.append(ARR[i])
  i += 1

A = list(set(A))
B = list(set(B))

print(len(A) + len(B))