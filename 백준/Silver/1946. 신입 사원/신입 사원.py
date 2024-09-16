import sys
read = sys.stdin.readline

T = int(read().rstrip())
for i in range(T):
  N = int(read().rstrip())
  ARR = [list(map(int, read().rstrip().split())) for _ in range(N)]
  
  arr = sorted(ARR, key=lambda x: x[0])
  cnt = 0
  minB = float('inf')
  for a, b in arr:
    if minB > b:
      cnt += 1
      minB = b
  
  print(cnt)