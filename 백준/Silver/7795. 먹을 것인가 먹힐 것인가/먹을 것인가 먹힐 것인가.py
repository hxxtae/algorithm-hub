import sys
read = sys.stdin.readline

T = int(read().rstrip())
for _ in range(T):
  N, M = map(int, read().rstrip().split())
  aArr = [*map(int, read().rstrip().split())]
  bArr = [*map(int, read().rstrip().split())]

  aArr.sort(key=lambda x: -x)
  bArr.sort(key=lambda x: -x)
  
  aidx = 0
  temp = 0
  answer = 0
  for bidx in range(M):
    while aidx < N and aArr[aidx] > bArr[bidx]:
      aidx += 1
      temp += 1
    
    answer += temp
  
  print(answer)

