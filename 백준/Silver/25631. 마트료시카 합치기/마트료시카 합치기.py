from collections import *
import sys
read = sys.stdin.readline

N = int(read().rstrip())
ARR = list(map(int, read().rstrip().split()))

obj = defaultdict(int)
for i in ARR:
  obj[i] += 1

print(max(obj.values()))