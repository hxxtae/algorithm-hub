import sys
from itertools import combinations
read = sys.stdin.readline

N, M = map(int, read().rstrip().split(' '))
MAP = [[*map(int, read().rstrip().split(' '))] for _ in range(N)]

house = []
chick = []
for r in range(N):
  for c in range(N):
    if MAP[r][c] == 1:
      house.append([r, c])
    if MAP[r][c] == 2:
      chick.append([r, c])

chickLen = float('inf')
for chickOfCom in combinations(chick, M):
  totalLen = 0
  for hou in house:
    roadLen = float('inf')
    # 집 <-> 치킨집 까지의 거리 비교 (최단 거리 추출)
    for i in range(M):
      roadLen = min(roadLen, abs(hou[0] - chickOfCom[i][0]) + abs(hou[1] - chickOfCom[i][1]))
    totalLen += roadLen

  # 모든 집과 분류된(M) 치킨집과의 최단거리
  chickLen = min(chickLen, totalLen)

print(chickLen)