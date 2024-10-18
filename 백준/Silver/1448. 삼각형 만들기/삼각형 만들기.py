import sys
read = sys.stdin.readline

N = int(read().rstrip())
ARR = [int(read().rstrip()) for _ in range(N)]

arr = sorted(ARR, key=lambda x: -x)
for i in range(N):
  if len(arr[i:i+3]) == 3:
    a, b, c = (arr[i], arr[i+1], arr[i+2])
    if a < b + c:
      print(a + b + c)
      exit()

print(-1)