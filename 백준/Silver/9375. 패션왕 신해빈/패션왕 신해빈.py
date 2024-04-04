import sys
from collections import defaultdict
read = sys.stdin.readline

T = int(read().rstrip())

for _ in range(T):
  N = int(read().rstrip())
  CLOTHES = [read().rstrip().split(' ') for _ in range(N)]
  
  result = 1
  categoryDict = defaultdict(int)
  for _, category in CLOTHES:
    categoryDict[category] += 1
  
  for cnt in categoryDict.values():
    result *= (cnt + 1)
  
  print(result-1)