import sys
read = sys.stdin.readline

N = int(read().rstrip())
arr = [*map(int, read().rstrip().split())]

answer = []
for i in range(N, 0, -1):
  left = answer[0:arr[i-1]]
  right = answer[arr[i-1]:N]
  answer = [*left, i, *right]

print(*answer)