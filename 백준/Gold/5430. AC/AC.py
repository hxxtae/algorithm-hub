import sys
from collections import deque
read = sys.stdin.readline

T = int(read().rstrip())
TESTCASE = [[read().rstrip() for _ in range(3)] for _ in range(T)]

for p, n, arr in TESTCASE:
  arr = arr[1:-1].split(',')
  if arr[0] == '':
    arr = []
  
  deq = deque(arr)
  cnt = 0
  state = True

  for c in p:
    if c == 'R':
      cnt += 1
    
    if c == 'D':
      if len(deq) == 0:
        state = False
        break
      # 홀수
      if cnt % 2 != 0:
        deq.pop()
      # 짝수
      if cnt % 2 == 0:
        deq.popleft()
  
  if state:
    if bool(cnt % 2):
      deq.reverse()
    print("["+",".join(deq)+"]")
  else:
    print('error')
  