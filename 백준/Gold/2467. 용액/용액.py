import sys
read = sys.stdin.readline

N = int(read().rstrip())
ARR = list(map(int, read().rstrip().split()))

min = float('inf')
left = 0
right = N - 1

for i, num in enumerate(ARR):
  start = i + 1
  end = N - 1
  if min == 0:
    break

  while start <= end:
    mid = (start + end) // 2
    
    curr = num + ARR[mid]
    currAbs = int(abs(curr))

    if currAbs < min:
      min = currAbs
      left = i
      right = mid
      if min == 0:
        break
    
    if curr < 0:
      start = mid + 1
    else:
      end = mid - 1

print(ARR[left], ARR[right])
