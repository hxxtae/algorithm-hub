import sys
read = sys.stdin.readline

N, L = map(int, read().rstrip().split())
ARR = [*map(int, read().rstrip().split())]

arr = sorted(ARR, key=lambda x: -x)
currNum = arr[0]
cnt = 1
for num in arr:
  if L <= (currNum - num):
    cnt += 1
    currNum = num

print(cnt)