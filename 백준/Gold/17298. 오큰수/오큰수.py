import sys
read = sys.stdin.readline

N = int(read().rstrip())
ARR = list(map(int, read().rstrip().split(' ')))

length = len(ARR)
answer = [-1] * length
stack = [ARR[-1]]

for i, num in enumerate(ARR[::-1]):
  if i == 0: continue
  
  maxRight = stack[-1]
  # maxRight가 더 큰 경우
  if maxRight > num:
    answer[length-1-i] = maxRight
    stack.append(num)
    continue
  
  # num이 더 큰 경우
  while stack:
    maxRight = stack[-1]
    if maxRight > num: 
      answer[length-1-i] = maxRight
      break
    stack.pop()
  stack.append(num)

print(*answer)