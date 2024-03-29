import sys
rl = sys.stdin.readline

A1, A0 = map(int, rl().rstrip().split(' '))
C = int(rl().rstrip())
N0 = int(rl().rstrip())

answer = 1
for n in range(N0, 100+1):
  fn1 = A1 * n + A0
  fn2 = n * C
  if fn1 <= fn2: continue
  answer = 0
  break

print(answer)
