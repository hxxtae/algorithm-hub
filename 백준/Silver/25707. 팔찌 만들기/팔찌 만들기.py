import sys
read = sys.stdin.readline

N = int(read().rstrip())
ARR = list(map(int, read().rstrip().split()))

count = 0
ARR.sort()
for i in range(1, N):
  count += abs(ARR[i] - ARR[i-1])
count += abs(ARR[N-1] - ARR[0])
print(count)
