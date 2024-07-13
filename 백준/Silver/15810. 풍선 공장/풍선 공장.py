import sys
read = sys.stdin.readline

N, M = map(int, read().rstrip().split())
T_ARR = list(map(int, read().rstrip().split()))

start = 0
end = max(T_ARR) * M
answer = 0

while start <= end:
  mid = (start + end) // 2 # M개의 풍선을 만드는데 걸리는 시간

  cnt = 0
  for time in T_ARR:
    cnt += mid // time

  if cnt >= M:
    end = mid - 1
    answer = mid
  else:
    start = mid + 1

print(answer)