import sys
read = sys.stdin.readline

N = int(read().rstrip())
ARR = list(map(int, read().rstrip().split()))

arr = sorted(ARR, key=lambda x: -x)
if len(arr) == 1: 
  print(0)
else:
  total = arr[0] + arr[1]
  for num in arr[2:]:
    total += (arr[0] + num)
  print(total)
