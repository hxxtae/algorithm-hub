from heapq import *
import sys
read = sys.stdin.readline

def solution(k, arr):
  answer = 0
  heapify(arr)
  while arr and len(arr) > 1:
    a, b = [heappop(arr), heappop(arr)]
    toSum = a + b
    heappush(arr, toSum)
    answer += toSum
  
  return answer

T = int(read().rstrip())
for _ in range(T):
  K = int(read().rstrip())
  ARR = [*map(int, read().rstrip().split())]
  print(solution(K, ARR))

