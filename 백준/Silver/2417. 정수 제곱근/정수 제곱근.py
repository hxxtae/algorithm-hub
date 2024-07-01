import sys
read = sys.stdin.readline

N = int(read().rstrip())

start = 0
end = N
answer = 0

while start <= end:
  mid = (start + end) // 2
  square = mid ** 2
  if square < N:
    start = mid + 1
    answer = mid + 1
  else:
    end = mid - 1

print(answer)
