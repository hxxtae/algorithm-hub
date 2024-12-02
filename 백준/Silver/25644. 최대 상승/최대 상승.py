import sys
read = sys.stdin.readline

N = int(read().rstrip())
ARR = list(map(int, read().rstrip().split()))

minPrice = float('inf')
answer = 0

for num in ARR:
  if minPrice < num: answer = max(answer, num - minPrice)
  else: minPrice = num

print(answer)