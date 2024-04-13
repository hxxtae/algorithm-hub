from heapq import *
import sys
read = sys.stdin.readline

N = int(read().rstrip())
ARR = [int(read().rstrip()) for _ in range(N)]

def stackFunc():
  answer = []
  stack = []
  idx = 0
  for a in range(1, N+1):
    stack.append(a)
    answer.append('+')

    while stack and a >= ARR[idx]:
      if stack[-1] != ARR[idx]: return print('NO')
      stack.pop()
      answer.append('-')
      idx += 1

  print("\n".join(answer))

stackFunc()