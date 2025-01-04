from collections import *
import sys
read = sys.stdin.readline

N, M, K = map(int, read().rstrip().split())
ARR = [list(map(float, read().rstrip().split())) for _ in range(M)]

nDict = defaultdict(int)
for nArr in ARR:
  for i in range(N):
    curr = i * 2
    n, m = int(nArr[curr]), nArr[curr + 1]
    nDict[n] = max(nDict[n], m)

kArr = sorted(nDict.values(), key=lambda x: -x)
print(round(sum(kArr[:K]), 1))
