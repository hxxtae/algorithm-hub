import sys
read = sys.stdin.readline

N = int(read().rstrip())
ARR = [int(read().rstrip()) for _ in range(N)]

maxNum = ARR[N-1]
cnt = 0
for num in ARR[::-1][1:]:
  if num >= maxNum:
    cnt += ((num - maxNum) + 1)
    maxNum -= 1
  else:
    maxNum = num
    
print(cnt)