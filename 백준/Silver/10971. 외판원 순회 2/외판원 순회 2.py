import sys
read = sys.stdin.readline

N = int(read().rstrip())
GRAPH = [[*map(int, read().rstrip().split())] for _ in range(N)]

visited = [0] * N
answer = float('inf')

def dfs(node, start, total, cnt):
  if cnt == N and node == start:
    global answer
    answer = min(answer, total)
    return

  for next in range(N):
    pay = GRAPH[node][next]
    if pay == 0: continue
    if visited[node]: continue
    visited[node] = 1
    total += pay
    if answer >= total:
      dfs(next, start, total, cnt + 1)
    total -= pay
    visited[node] = 0

for start in range(N):
  dfs(start, start, 0, 0)

print(answer)

