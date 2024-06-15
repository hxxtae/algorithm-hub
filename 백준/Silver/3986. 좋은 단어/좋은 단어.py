from collections import deque
import sys
read = sys.stdin.readline

N = int(read().rstrip())
N_LIST = [read().rstrip() for _ in range(N)]

cnt = 0
for r in range(N):
  stack = deque([])
  for c in N_LIST[r]:
    if not len(stack):
      stack.append(c)
    elif stack[-1] == c:
      stack.pop()
    else:
      stack.append(c)

  if not len(stack):
    cnt += 1

print(cnt)