import sys
read = sys.stdin.readline

N, M = map(int, read().rstrip().split())
lectures = [*map(int, read().rstrip().split())]

start = max(lectures)
end = sum(lectures)

answer = 0
while start <= end:
  mid = (start + end) // 2

  total = 0
  cnt = 1
  for time in lectures:
    if (total + time) > mid:
      total = 0
      cnt += 1
    total += time
  
  if cnt <= M:
    end = mid - 1
    answer = mid
  else:
    start = mid + 1

print(answer)
