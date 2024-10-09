import sys
read = sys.stdin.readline

N = int(read().rstrip())
ARR = [int(read().rstrip()) for _ in range(N)]

ARR.sort()
answer = 0
for i in range(N):
  answer += abs((i+1) - ARR[i])
print(answer)