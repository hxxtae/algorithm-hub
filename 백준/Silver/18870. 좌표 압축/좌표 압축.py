import sys
read = sys.stdin.readline

N = int(read().rstrip())
ARR = [*map(lambda x: [int(x[0]), int(x[1])], enumerate(read().rstrip().split(' ')))]

ARR = sorted(ARR, key=lambda x: x[1])
score = -1
prev = float('inf')
for arr in ARR:
  if prev != arr[1]:
    score += 1
  arr.append(score)
  prev = arr[1]

ARR = sorted(ARR, key=lambda x: x[0])
print(" ".join(map(lambda x: str(x[2]), ARR)))