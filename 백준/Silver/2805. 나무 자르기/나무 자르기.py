import sys
read = sys.stdin.readline

N, M = map(int, read().rstrip().split())
TREES = [*map(int, read().rstrip().split())]

TREES.sort()
start = 0
end = TREES[-1]

while start <= end:
  half = (start + end) // 2
  length = 0

  for tree in TREES:
    if tree <= half: continue
    length += (tree - half)
  
  if length >= M:
    start = half + 1
  else:
    end = half - 1

print(end)