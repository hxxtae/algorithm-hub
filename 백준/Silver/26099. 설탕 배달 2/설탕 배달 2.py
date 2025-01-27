import sys
read = sys.stdin.readline

N = int(read().rstrip())

answer = 0
while N % 5:
  N -= 3
  answer += 1

if N < 0:
  print(-1)
else:
  print(answer + (N // 5))