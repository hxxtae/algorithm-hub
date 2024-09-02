import sys
read = sys.stdin.readline

N = int(read().rstrip())

suger = N
answer = 0
while suger > 0:
  if suger % 5 == 0:
    answer += suger // 5
    suger = 0
    break
  suger -= 3
  answer += 1

if suger == 0:
  print(answer)
else:
  print(-1)