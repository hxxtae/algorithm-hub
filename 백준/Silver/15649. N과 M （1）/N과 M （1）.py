import sys
rl = sys.stdin.readline

N, M = map(int, rl().rstrip().split(' '))

visited = [0] * N
nums = list(range(1, N+1))
arr = []
answer = ""

def dfs(cnt):
  if cnt == M:
    print(*arr)
    return

  for i, num in enumerate(nums):
    if visited[i]: continue
    visited[i] = 1
    arr.append(num)
    dfs(cnt + 1)
    arr.pop()
    visited[i] = 0

dfs(0)