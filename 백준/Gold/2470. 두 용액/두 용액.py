import sys
read = sys.stdin.readline

N = int(read().rstrip())
ARR = [*map(int, read().rstrip().split(' '))]

ARR.sort()
start = 0
end = len(ARR) - 1
minZero = abs(ARR[start] + ARR[end])
answerLeft = ARR[start]
answerRight = ARR[end]

while start < end:
  left = ARR[start]
  right = ARR[end]
  sumOne = left + right

  if abs(sumOne) < minZero:
    minZero = abs(sumOne)
    answerLeft = left
    answerRight = right
    if minZero == 0:
      break
  
  if sumOne < 0:
    start += 1
  
  if sumOne >= 0:
    end -= 1

print(answerLeft, answerRight)