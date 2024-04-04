from functools import reduce
import sys
read = sys.stdin.readline

N = int(read().rstrip())
ARR = [*map(int, read().rstrip().split(' '))]

ARR.sort()
prev = 0
answer = []
for num in ARR:
  answer.append(prev + num)
  prev += num

print(sum(answer))