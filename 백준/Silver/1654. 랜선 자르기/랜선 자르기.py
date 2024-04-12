import sys
read = sys.stdin.readline

K, N = [*map(int, read().rstrip().split())]
ARR = [int(read().rstrip()) for _ in range(K)]

start = 1
end = max(ARR)

while start <= end:
  half = (start + end) // 2
  cnt = 0
  for length in ARR:
    cnt += length // half

  if cnt >= N:
    start = half + 1
  else:
    end = half - 1

print(end)