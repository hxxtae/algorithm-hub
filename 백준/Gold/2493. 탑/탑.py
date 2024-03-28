import sys
rl = sys.stdin.readline

N = int(rl().rstrip())
TOPS = list(map(int, rl().rstrip().split(' ')))

answer = [0] * N
stack = []

for i, top in enumerate(TOPS):
    
  while len(stack) and stack[-1][1] <= top:
    stack.pop()
  
  if len(stack):
    answer[i] = stack[-1][0]
  
  stack.append([i + 1, top])

print(" ".join(map(str, answer)))
