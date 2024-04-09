from collections import deque
import sys
read = sys.stdin.readline

N, K = map(int, read().rstrip().split())
maxNum = 100001
visited = [0] * maxNum

def findWay(x, way):
  X = [1, -1, 2*x, -2*x]
  if way >= 2:
    return X[way]
  return x + X[way]

def bfs(startX):
  queue = deque([[startX, 0]])
  visited[startX] = 1
  answer = 0

  while queue:
    x, cnt = queue.popleft()

    if x == K:
      answer = cnt
      break

    for i in range(4):
      nextX = findWay(x, i)
      if nextX < 0 or nextX >= maxNum: continue
      if visited[nextX]: continue
      visited[nextX] = 1
      queue.append([nextX, cnt + 1])

  return answer

print(bfs(N))


