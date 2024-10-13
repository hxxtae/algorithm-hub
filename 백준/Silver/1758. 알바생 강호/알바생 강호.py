import sys
read = sys.stdin.readline

N = int(read().rstrip())
ARR = [int(read().rstrip()) for _ in range(N)]

arr = sorted(ARR, key=lambda x: -x)
answer = 0
for i, tip in enumerate(arr):
  rev = tip - i
  if rev < 0:
    break
  answer += rev

print(answer)