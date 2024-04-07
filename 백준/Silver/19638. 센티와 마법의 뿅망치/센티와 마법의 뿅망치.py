from heapq import *
import sys
read = sys.stdin.readline

N, H, T = map(int, read().rstrip().split(' '))
GIANTS = [int(read().rstrip()) for _ in range(N)]

tallGiants = sorted(map(lambda item: -item, [*filter(lambda x: x >= H, GIANTS)]))
cnt = 0

while T and tallGiants:
  if -tallGiants[0] == 1: break

  tall = heappop(tallGiants)
  tall = abs(tall) // 2
  if tall >= H:
    heappush(tallGiants, -tall)

  T -= 1
  cnt += 1

if len(tallGiants) == 0:
  print('YES')
  print(cnt)
else:
  print('NO')
  print(-tallGiants[0])
