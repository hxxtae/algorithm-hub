import sys
read = sys.stdin.readline

N, S = map(int, read().rstrip().split())
ARR = [*map(int, read().rstrip().split())]

cnt = 0
def dfs(deep, arr):
  if arr and S == sum(arr):
    global cnt
    cnt += 1

  for i in range(deep, N):
    node = ARR[i]
    arr.append(node)
    dfs(i + 1, arr)
    arr.pop()
  
dfs(0, [])

print(cnt)