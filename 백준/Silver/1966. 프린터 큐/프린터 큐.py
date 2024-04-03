import sys
from collections import deque
read = sys.stdin.readline

T = int(read().rstrip())
PRINTS = [[[*map(int, read().rstrip().split(' '))] for _ in range(2)] for _ in range(T)]

answer = []
for (n, m), file in PRINTS:
  # n:문서개수, m:찾는문서, file:문서
  # fileImp: 문서 중요도 종류 (내림차순)
  # fileMap: 문서들 => [위치, 중요도]
  fileImp = sorted(file, key=(lambda x: -x))
  fileMap = list(map(lambda x: [*x], enumerate(file)))
  deqFile = deque(fileMap)
  cnt = 0
  for imp in fileImp:
    
    while imp != deqFile[0][1]:
      deqFile.append(deqFile.popleft())
    
    if deqFile[0][1] == imp:
      cnt += 1
      idx, num = deqFile.popleft()
      
      if idx == m:
        answer.append(cnt)
        break

print('\n'.join(map(str, answer)))