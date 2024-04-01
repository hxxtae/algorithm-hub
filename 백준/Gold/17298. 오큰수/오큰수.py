import sys
read = sys.stdin.readline

N = int(read().rstrip())
ARR = list(map(int, read().rstrip().split(' ')))

length = len(ARR)
answer = [-1] * length
stack = [ARR[-1]]

for i in range(length-2, -1, -1):
  num = ARR[i]

  maxRight = stack[-1]
  # maxRight가 더 큰 경우
  if maxRight > num:
    answer[i] = maxRight
    stack.append(num)
    continue
  
  # num이 더 큰 경우
  while stack:
    maxRight = stack[-1]
    if maxRight > num: 
      answer[i] = maxRight
      break
    stack.pop()
  stack.append(num)

print(*answer)