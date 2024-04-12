import sys
read = sys.stdin.readline

N = int(read().rstrip())

answer = 0
stack = []
for _ in range(N):
  num = int(read().rstrip())
  if num == 0:
    answer -= stack.pop()
    continue

  stack.append(num)
  answer += num

print(answer)