import sys
read = sys.stdin.readline

N = int(read().rstrip())
M = int(read().rstrip())
X_ARR = [*map(int, read().rstrip().split())]

prevX = X_ARR[0]
height = X_ARR[0]

for i in range(1, M):
  currX = X_ARR[i]
  dist = abs(prevX - currX)

  if dist % 2 == 0:
    dist = dist // 2 # 양쪽 가로등이 불빛을 비추기 때문에 2로 나눈다.
  else:
    dist = (dist // 2) + 1
  
  height = max(height, dist)
  prevX = currX

height = max(height, abs(N - X_ARR[-1]))

print(height)