import sys
read = sys.stdin.readline

N = int(read().rstrip())
ARR = list(map(int, read().rstrip().split()))

LIS = [ARR[0]]
for n in ARR[1:]:
  if LIS[-1] < n:
    LIS.append(n)
  else:
    left = 0
    right = len(LIS) - 1
    index = left
    
    while left <= right:
      mid = (left + right) // 2
      
      if n <= LIS[mid]:
        right = mid - 1
        index = mid
      else:
        left = mid + 1
    
    LIS[index] = n # 중요한 건 LIS의 길이 이다.
  
print(len(LIS))
