import sys
rl = sys.stdin.readline

N, M = list(map(int, rl().rstrip().split(' ')))
NUMS = sorted(map(int, rl().rstrip().split(' ')))

answer = ""
arr = []
visited = [0] * N

def dfs(cnt):
  if cnt == M:
    global answer
    print(*arr)
    return
  
  check = -1

  for i, num in enumerate(NUMS):
    if visited[i]: continue
    if check == num: continue
    visited[i] = 1
    arr.append(num)
    check = num
    dfs(cnt + 1)
    arr.pop()
    visited[i] = 0

dfs(0)