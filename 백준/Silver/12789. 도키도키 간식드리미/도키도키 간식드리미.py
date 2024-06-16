from collections import deque
import sys
read = sys.stdin.readline

N = int(read().rstrip())
line = deque([*map(int, read().rstrip().split())])

curr = 1
stand_line = []

while line:
  num = line.popleft()
  if curr == num:
    curr += 1
  else:
    while stand_line:
      if curr == stand_line[-1]:
        stand_line.pop()
        curr += 1
      else:
        break
    stand_line.append(num)

while stand_line:
  num = stand_line.pop()
  if curr == num:
    curr += 1
  else:
    print("Sad")
    exit(0)

print("Nice")
