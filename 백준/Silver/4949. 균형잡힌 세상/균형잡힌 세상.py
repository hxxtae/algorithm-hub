from collections import deque
import sys
read = sys.stdin.readline

strDict = ["(", ")", "[", "]"]
while True:
  readStr = read().rstrip()
  if '.' in readStr[0]: break
  stack = deque([])
  for s in readStr:
    if s not in strDict: continue
    if s in '(' or s in '[':
      stack.append(s)
      continue
    
    if stack and stack[-1] == "(" and s == ")":
      stack.pop()
      continue
    if stack and stack[-1] == "[" and s == "]":
      stack.pop()
      continue

    stack.append(s)

  if stack:
    print('no')
  else:
    print('yes')