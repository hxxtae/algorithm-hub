import sys
read = sys.stdin.readline

M, N = map(int, read().rstrip().split())
snacks = [*map(int, read().rstrip().split())]

start = 1
end = max(snacks)
answer = 0

while start <= end:
  mid = (start + end) // 2

  cnt = 0
  for length in snacks:
    if length >= mid:
      cnt += length // mid
  
  if cnt >= M:
    start = mid + 1
    answer = mid
  else:
    end = mid - 1

print(answer)

