import sys
read = sys.stdin.readline

N = int(read().rstrip())
ARR = list(map(int, read().rstrip().split()))

ARR.sort()
answer = 0

for i, num in enumerate(ARR):
  temps = ARR[:i] + ARR[i+1:]
  start = 0
  end = len(temps) - 1
  
  while start < end:
    sumNum = temps[start] + temps[end]

    if num == sumNum:
      answer += 1
      break

    if num > sumNum:
      start += 1
    else:
      end -= 1

print(answer)
