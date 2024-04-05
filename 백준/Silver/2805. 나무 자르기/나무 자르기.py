import sys
read = sys.stdin.readline

N, M = map(int, read().rstrip().split(' '))
TREE = [*map(int, read().rstrip().split(' '))]

treeMin = 0
treeMax = max(TREE)
treeHalf = 0
lengthSum = 0

while treeMin <= treeMax:
  treeHalf = (treeMax + treeMin) // 2
  for num in TREE:
    if num >= treeHalf:
      lengthSum += (num - treeHalf)
  
  if lengthSum >= M:
    treeMin = treeHalf + 1
  
  if lengthSum < M:
    treeMax = treeHalf - 1

  lengthSum = 0

print(treeMax)