import sys
read = sys.stdin.readline

N, K = map(int, read().rstrip().split());
X_ARR = [int(read().rstrip()) for _ in range(N)]

X_ARR.sort()

start = min(X_ARR)
end = max(X_ARR) + K
answer = 0

while start <= end:
  mid = (start + end) // 2 # T: 팀 목표레벨
  
  total = 0 # 레벨을 올린 총합
  for x in X_ARR:
    if x >= mid:
      break

    total += mid - x
  
  if K >= total:
    start = mid + 1
    answer = max(answer, mid)
  else:
    end = mid - 1

print(answer)