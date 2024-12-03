import sys
read = sys.stdin.readline

N = int(read().rstrip())
ARR = list(map(int, read().rstrip().split()))

minSpeed = 0
totalSpeed = 0
for num in ARR[::-1]:
  if minSpeed < num:
    minSpeed += 1
    totalSpeed += minSpeed
  elif minSpeed > num:
    minSpeed = num
    totalSpeed += num
  else:
    totalSpeed += minSpeed

print(totalSpeed)