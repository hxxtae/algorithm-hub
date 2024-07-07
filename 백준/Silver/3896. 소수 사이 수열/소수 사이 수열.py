import sys
read = sys.stdin.readline

MIN_K = 2
MAX_K = 1_299_709

# 에라토스테네스의 체(소수 구하기)
decimal = [True] * (MAX_K + 1)
decimal[0], decimal[1] = False, False
for i in range(1, MAX_K + 1):
  if not decimal[i]: 
    continue

  for j in range(i * i, MAX_K + 1, i):
    decimal[j] = False

T = int(read().rstrip())
for _ in range(T):
  K = int(read().rstrip())

  if decimal[K]:
    print(0)
    continue

  # left
  cnt = 2
  left = K
  right = K

  while True:
    left -= 1
    if decimal[left]:
      break
    cnt += 1
  
  # right
  while True:
    right += 1
    if decimal[right]:
      break
    cnt += 1
  
  print(cnt)
