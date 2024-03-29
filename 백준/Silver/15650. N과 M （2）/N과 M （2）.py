import sys
rl = sys.stdin.readline

N, M = list(map(int, rl().rstrip().split(' ')))

arr = []
visited = [0] * N
nums = list(map(str, range(1, N+1)))
answer = []

def dfs(deep, cnt):
  if cnt == M:
    answer.append(" ".join(arr))
    return

  i = deep
  while i < N:
    num = nums[i]
    if visited[i]:
      i += 1
      continue
    visited[i] = 1
    arr.append(num)
    dfs(i + 1, cnt + 1)
    arr.pop()
    visited[i] = 0
    i += 1

dfs(0, 0)
print("\n".join(answer))