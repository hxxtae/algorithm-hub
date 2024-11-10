from collections import deque
import sys
read = sys.stdin.readline

T = int(read().rstrip())
for _ in range(T):
  N = int(read().rstrip())
  ARR = read().rstrip().split()
  
  dq = deque([ARR[0]])
  for c in ARR[1:]:
    if dq[0] >= c: dq.appendleft(c)
    else: dq.append(c)

  print(''.join(dq))