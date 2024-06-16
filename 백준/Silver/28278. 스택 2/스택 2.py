import sys
read = sys.stdin.readline

N = int(read().rstrip())
ORDERS = [[*map(int, read().rstrip().split())] for _ in range(N)]

stack = []

# 1
def addNum(num):
  stack.append(num)

# 2
def popNum():
  if not len(stack):
    print(-1)
  else:
    print(stack.pop())

# 3
def getSize():
  print(len(stack))

# 4
def confirmEmpty():
  if len(stack):
    print(0)
  else:
    print(1)

# 5
def getNum():
  if len(stack):
    print(stack[-1])
  else:
    print(-1)

for arr in ORDERS:
  order = arr[0]
  if order == 1:
    addNum(arr[1])
  elif order == 2:
    popNum()
  elif order == 3:
    getSize()
  elif order == 4:
    confirmEmpty()
  else:
    getNum()
