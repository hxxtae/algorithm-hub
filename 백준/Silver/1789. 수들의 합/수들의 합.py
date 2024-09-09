import sys
read = sys.stdin.readline

S = int(read().rstrip())

answer = 0
num = 0
while True:
  num += 1
  answer += num
  if answer > S:
    break

print(num - 1)