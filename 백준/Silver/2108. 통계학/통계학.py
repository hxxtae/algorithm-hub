from collections import defaultdict
import sys
read = sys.stdin.readline

N = int(read().rstrip())
ARR = [int(read().rstrip()) for _ in range(N)]

# 산술평균: N개의 수들의 합을 N으로 나눈 값
print(round(sum(ARR) / N))

# 중앙값: N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
print(sorted(ARR)[N//2])

# 최빈값: N개의 수들 중 가장 많이 나타나는 값
obj = defaultdict(int)
for i in range(N):
  obj[ARR[i]] += 1

maxCnt = max(obj.values())
objFilter = [*filter(lambda x: maxCnt == x[1], obj.items())]
objFilter = sorted(objFilter, key=lambda x: x[0])
if len(objFilter) == 1:
  print(objFilter[0][0])
else: 
  print(objFilter[1][0])

# 범위: N개의 수들 중 최댓값과 최솟값의 차이
print(max(ARR) - min(ARR))