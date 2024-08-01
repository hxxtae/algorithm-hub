import sys
read = sys.stdin.readline

while 1:
  N = int(read().rstrip())
  if N == 0: break
  
  start = 1
  end = 50
  answer = []
  
  while start <= end:
    mid = (start + end) // 2
    
    if N > mid:
      start = mid + 1
    elif N < mid:
      end = mid - 1
    else:
      answer.append(mid)
      break

    answer.append(mid)

  print(*answer)
