import sys
read = sys.stdin.readline

N = int(read().rstrip())
ARR = [*map(int, read().rstrip().split())]

arr = sorted(ARR, key=lambda x: -x)
answer = arr[0]
for i in range(1, N):
  answer += (arr[i] / 2)

print(answer)