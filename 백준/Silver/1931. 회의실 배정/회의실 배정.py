import sys
read = sys.stdin.readline

L = int(read().rstrip())
LARR = [[*map(int, read().rstrip().split())] for _ in range(L)]

LARR = sorted(LARR, key=lambda x: (x[1], x[0]))
answer = 1
prev_s, prev_e = LARR[0]
for s, e in LARR[1:]:
  if s >= prev_e:
    answer += 1
    prev_s = s
    prev_e = e
  else:
    continue

print(answer)

