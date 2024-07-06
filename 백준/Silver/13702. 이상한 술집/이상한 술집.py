import sys
read = sys.stdin.readline

K, N = map(int, read().rstrip().split())
bottles = [int(read().rstrip()) for _ in range(K)]

start = 1
end = max(bottles)
answer = end

while start <= end:
  mid = (start + end) // 2 # 막걸리 용량

  cnt = 0
  for bottle in bottles:
    cnt += (bottle // mid)

  if cnt >= N:
    start = mid + 1
    answer = mid
  else:
    end = mid - 1

print(answer)