import sys
read = sys.stdin.readline

def solution(n, arrN, m, arrM):
  arrN = sorted(arrN)
  answer = [0] * m
  
  for i, num in enumerate(arrM):
    start = 0
    end = len(arrN)-1

    while start <= end:
      half = (start + end) // 2
      
      if num == arrN[half]:
        answer[i] = 1
        break

      if num >= arrN[half]:
        start = half + 1
      elif num < arrN[half]:
        end = half - 1
  
  print("\n".join(map(str, answer)))


T = int(read().rstrip())
for _ in range(T):
  N = int(read().rstrip())
  ARR_N = [*map(int, read().rstrip().split())]
  M = int(read().rstrip())
  ARR_M = [*map(int, read().rstrip().split())]
  solution(N, ARR_N, M, ARR_M)