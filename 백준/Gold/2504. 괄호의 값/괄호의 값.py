import sys
read = sys.stdin.readline

ARR = read().rstrip()
stack = []
temp = 1
answer = 0

for i in range(len(ARR)):
  if ARR[i] == "(":
    stack.append(ARR[i])
    temp *= 2
  elif ARR[i] == "[":
    stack.append(ARR[i])
    temp *= 3

  elif ARR[i] == ")":
    if not stack or stack[-1] == "[":
      answer = 0
      break
    if ARR[i-1] == "(":
      answer += temp
    temp //= 2
    stack.pop()

  elif ARR[i] == "]":
    if not stack or stack[-1] == "(":
      answer = 0
      break
    if ARR[i-1] == "[":
      answer += temp
    temp //= 3
    stack.pop()

if stack:
  print(0)
else:
  print(answer)
