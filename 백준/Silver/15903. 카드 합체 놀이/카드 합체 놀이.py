import sys
from heapq import *
read = sys.stdin.readline

N, M = map(int, read().rstrip().split(' '))
CARDS = [*map(int, read().rstrip().split(' '))]

heapify(CARDS)
for _ in range(M):
  abSum = (heappop(CARDS) + heappop(CARDS))
  heappush(CARDS, abSum)
  heappush(CARDS, abSum)

print(sum(CARDS))
