import sys
read = sys.stdin.readline

N = int(read().rstrip())
heightArr = list(map(int, read().rstrip().split()))
speedArr = list(map(int, read().rstrip().split()))

arr = [[speedArr[i], heightArr[i]] for i in range(N)]
arr.sort()

answer = 0
for i in range(N):
  answer += ((arr[i][0] * i) + arr[i][1])

print(answer)
