import sys
read = sys.stdin.readline

N = int(read().rstrip())
COMMANDS = [read().rstrip().split() for _ in range(N)]

stack = []

def stackEmpty(arr):
  return 0 if len(arr) else 1

def stackPush(num, arr):
  arr.append(num)

def stackPop(arr):
  return -1 if stackEmpty(arr) else arr.pop()

def stackSize(arr):
  return len(arr)

def stackTop(arr):
  return -1 if stackEmpty(arr) else arr[-1]

for item in COMMANDS:
  command = item[0]
  if command == 'push':
    stackPush(item[1], stack)
  if command == 'pop':
    print(stackPop(stack))
  if command == 'size':
    print(stackSize(stack))
  if command == 'empty':
    print(stackEmpty(stack))
  if command == 'top':
    print(stackTop(stack))
