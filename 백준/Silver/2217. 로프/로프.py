import sys
read = sys.stdin.readline

N = int(read().rstrip())
ARR = [int(read().rstrip()) for _ in range(N)]

arr = sorted(ARR, key=lambda x: -x)
answer = 0
for i, num in enumerate(arr):
  w = ((i+1) * num)
  if answer < w:
    answer = w

print(answer)