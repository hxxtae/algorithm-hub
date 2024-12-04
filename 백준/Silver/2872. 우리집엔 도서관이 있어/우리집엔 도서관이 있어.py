import sys
read = sys.stdin.readline

N = int(read().rstrip())
ARR = [int(read().rstrip()) for _ in range(N)]

targetNum = N
answer = 0
for num in ARR[::-1]:
  if num == targetNum:
    targetNum -= 1
  else:
    answer += 1

print(answer)