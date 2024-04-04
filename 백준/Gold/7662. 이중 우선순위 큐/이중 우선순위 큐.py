import sys
from heapq import *
read = sys.stdin.readline

T = int(read().rstrip())
for _ in range(T):
  K = int(read().rstrip())
  maxHeap = []
  minHeap = []
  visited = [0] * K

  for i in range(K):
    ORDER, NUM = read().rstrip().split(' ')
    num = int(NUM)

    if ORDER == "I":
      heappush(maxHeap, [-num, i])
      heappush(minHeap, [num, i])
      visited[i] = 1
      continue
    
    if ORDER == "D" and num == 1:
      while maxHeap and not visited[maxHeap[0][1]]:
        heappop(maxHeap)
      if maxHeap:
        visited[maxHeap[0][1]] = 0
        heappop(maxHeap)
      
    if ORDER == "D" and num == -1:
      while minHeap and not visited[minHeap[0][1]]:
        heappop(minHeap)
      if minHeap:
        visited[minHeap[0][1]] = 0
        heappop(minHeap)
  
  while maxHeap and not visited[maxHeap[0][1]]: heappop(maxHeap)
  while minHeap and not visited[minHeap[0][1]]: heappop(minHeap)
  if maxHeap and minHeap:
    print(str(-maxHeap[0][0]) + " " + str(minHeap[0][0]))
  else:
    print("EMPTY")
