import sys
read = sys.stdin.readline

N, K = map(int, read().rstrip().split())
ARR = list(map(int, read().rstrip().split()))

ARR.sort()
start = 0
end = N-1
answer = 0
while start < end:
  if K >= (ARR[start] + ARR[end]):
    start += 1
    end -= 1
    answer += 1
  else:
    end -= 1

print(answer)