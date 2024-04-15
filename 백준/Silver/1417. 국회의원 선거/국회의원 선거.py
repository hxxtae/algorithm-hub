from heapq import *
import sys
read = sys.stdin.readline

N = int(read().rstrip())
VOTES = [int(read().rstrip()) for _ in range(N)]

vote1 = VOTES.pop(0)
heap = [*map(lambda x: -x, VOTES)]
heapify(heap)
cnt = 0
while heap and -heap[0] >= vote1:
  vote = heappop(heap)
  heappush(heap, vote+1)
  vote1 += 1
  cnt += 1

print(cnt)
