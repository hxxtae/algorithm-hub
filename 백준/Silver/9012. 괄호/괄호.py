import sys
read = sys.stdin.readline

N = int(read().rstrip())
BRACKET = [read().rstrip() for _ in range(N)]

for bracket in BRACKET:
  stack = []
  for b in bracket:
    # 1. '(' 모양은 stack에 쌓기
    if b == '(':
      stack.append(b)
      continue

    # 2. ')' 모양은 stack 맨 끝에 '('가 있으면 pop
    if b == ')' and len(stack) > 0:
      if stack[-1] == '(':
        stack.pop()
      continue

    stack.append(b)
  
  if len(stack):
    print('NO')
  else:
    print("YES")
