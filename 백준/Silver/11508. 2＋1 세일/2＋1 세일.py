import sys
read = sys.stdin.readline

N = int(read().rstrip())
ARR = [int(read().rstrip()) for _ in range(N)]

arr = sorted(ARR, key=lambda x: -x)
answer = 0
for i, num in enumerate(arr):
  if (i + 1) % 3 == 0:
    continue
  answer += num

print(answer)