from collections import deque
import sys
read = sys.stdin.readline

N, M = map(int, read().rstrip().split(' '))
LADDERS = [[*map(int, read().rstrip().split(' '))] for _ in range(N)]
SNAKES = [[*map(int, read().rstrip().split(' '))] for _ in range(M)]

board = [num for num in range(0, 101)]
visited = [0] * 101

ladderDict = {arr[0]: arr[1] for arr in LADDERS}
snakeDict = {arr[0]: arr[1] for arr in SNAKES}

def bfs(startNum):
  queue = deque([[startNum, 0]])
  visited[startNum] = 1
  answer = 0

  while queue:
    [num, cnt] = queue.popleft()
    if num == 100:
      answer = cnt
      break

    for i in range(1, 7):
      next = num + i
      if next in ladderDict:
        next = ladderDict[next]
      if next in snakeDict:
        next = snakeDict[next]
      
      if next < 1 or next > 100: continue
      if visited[next]: continue
      visited[next] = 1
      queue.append([next, cnt + 1])
  
  return answer

print(bfs(1))
