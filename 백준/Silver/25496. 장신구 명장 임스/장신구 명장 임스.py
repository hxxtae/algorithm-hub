import sys
read = sys.stdin.readline

P, N = map(int, read().rstrip().split())
ARR = list(map(int, read().rstrip().split()))

ARR.sort()
count = 0
for fg in ARR:
  if P >= 200: break
  P += fg
  count += 1

print(count)
