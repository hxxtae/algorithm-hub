import sys
read = sys.stdin.readline

N, M = map(int, read().rstrip().split())
jewels = [int(read().rstrip()) for _ in range(M)]

start = 1
end = max(jewels)
answer = start

while start <= end:
  mid = (start + end) // 2

  cnt = 0
  for jewel in jewels:
    if jewel % mid == 0:
      cnt += (jewel // mid)
    else:
      cnt += (jewel // mid + 1)
  
  if cnt > N:
    start = mid + 1
  else: # mid의 최솟값을 구해야 한다.
    end = mid - 1
    answer = mid

print(answer)