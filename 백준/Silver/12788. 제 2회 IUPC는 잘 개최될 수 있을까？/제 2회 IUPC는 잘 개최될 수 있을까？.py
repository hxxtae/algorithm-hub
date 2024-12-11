import sys
read = sys.stdin.readline

N = int(read().rstrip())
M, K = map(int, read().rstrip().split())
ARR = list(map(int, read().rstrip().split()))

pens = sorted(ARR, key=lambda x: -x)
member = M * K
count = 0
answer = 0
for pen in pens:
  if count >= member:
    break
  count += pen
  answer += 1

if count >= member:
  print(answer)
else:
  print("STRESS")