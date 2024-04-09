from collections import deque
import sys
read = sys.stdin.readline

N = int(read().rstrip())
LINE = [[*map(int, read().rstrip().split())] for _ in range(N)]

stack = [arr[1] for arr in LINE]
deq = deque([])

cnt = 0
for i in stack:
  while deq and deq[-1] > i:
    deq.pop()

  if len(deq) == 0:
    if i == 0: continue
    deq.append(i)
    cnt += 1
    continue

  if deq[-1] < i:
    cnt += 1

  deq.append(i)

print(cnt)