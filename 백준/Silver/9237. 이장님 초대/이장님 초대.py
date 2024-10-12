import sys
read = sys.stdin.readline

N = int(read().rstrip())
ARR = [*map(int, read().rstrip().split())]

arr = sorted(ARR, key=lambda x: -x)
remainDay = arr[0]

for d in arr:
  if remainDay < d:
    remainDay = d
  remainDay -= 1

print(remainDay + N + 2)