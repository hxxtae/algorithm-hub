import sys
read = sys.stdin.readline

N = int(read().rstrip())
ARR = [read().rstrip() for _ in range(N)]

ARR.sort(key=len)
answer = N
for i, si in enumerate(ARR):
  for j, sj in enumerate(ARR[i+1:]):
    if si in sj[:len(si)]:
      answer -= 1
      break

print(answer)