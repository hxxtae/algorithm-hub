import sys
read = sys.stdin.readline

N = int(read().rstrip())
ARR = list(map(int, read().rstrip().split()))

arr = [0] * N
count = 0
for i in range(N):
  if ARR[i] != arr[i]:
    arr[i] = int(not bool(arr[i]))
    if i + 1 < N: arr[i+1] = int(not bool(arr[i+1]))
    if i + 2 < N: arr[i+2] = int(not bool(arr[i+2]))
    count += 1

print(count)