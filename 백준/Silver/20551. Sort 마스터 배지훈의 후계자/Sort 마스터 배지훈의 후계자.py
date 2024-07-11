import sys
read = sys.stdin.readline

N, M = map(int, read().rstrip().split())
N_ARR = [int(read().rstrip()) for _ in range(N)]
M_ARR = [int(read().rstrip()) for _ in range(M)]

N_ARR.sort()

for d in M_ARR:
  start = 0
  end = len(N_ARR) - 1
  answer = -1

  while start <= end:
    mid = (start + end) // 2 # mid == index
    
    b = N_ARR[mid]
    if b >= d:
      end = mid - 1
      if b == d:
        answer = mid
    else:
      start = mid + 1
  
  print(answer)
