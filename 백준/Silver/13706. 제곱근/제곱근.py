import sys
read = sys.stdin.readline

N = int(read().rstrip())

start = 1
end = N

while start <= end:
  mid = (start + end) // 2

  if mid ** 2 == N:
    print(mid)
    break

  if mid ** 2 < N:
    start = mid + 1
  else:
    end = mid - 1
