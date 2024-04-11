from collections import deque
import sys
read = sys.stdin.readline

# -------------
#  입력
# -------------
N, M = [*map(int, read().rstrip().split())]
COMPUTERS = [[*map(int, read().rstrip().split())] for _ in range(M)]

# -------------
#  풀이 BFS
# -------------
graph = [[] for _ in range(N+1)]
for a, b in COMPUTERS:
  graph[b].append(a)

def bfs(startCom):
  queue = deque([startCom])
  visited = [0] * (N+1)
  visited[startCom] = 1

  cnt = 0
  while queue:
    com = queue.popleft()
    
    cnt += 1
    for next in graph[com]:
      if visited[next]: continue
      visited[next] = 1
      queue.append(next)
  
  return cnt

answer = []
maxCnt = 0
for com in range(1, N+1):
  cnt = bfs(com)
  if maxCnt == cnt:
    answer.append(com)
    
  if maxCnt < cnt:
    maxCnt = cnt
    answer = [com]

print(*sorted(answer))