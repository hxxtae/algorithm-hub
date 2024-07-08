import sys
read = sys.stdin.readline

N, L, W, H = map(int, read().rstrip().split())

start = 0
end = max(L, W, H)
answer = start

for _ in range(100):
  mid = (start + end) / 2 # mid는 A (한 변의 길이)

  cnt = (L // mid) * (W // mid) * (H // mid)
  if cnt >= N:
    start = mid
    answer = mid
  else:
    end = mid

print(answer)