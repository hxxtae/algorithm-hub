from collections import deque
import sys
read = sys.stdin.readline

N = int(read().rstrip())
GRAPH = [read().rstrip() for _ in range(N)]

# 0동, 1서, 2남, 3북
def findWay(y, x, way):
  X = [1, -1, 0, 0]
  Y = [0, 0, 1, -1]
  return [y + Y[way], x + X[way]]

def bfs(startY, startX, endY, endX):
  queue = deque([])
  visited = [[[-1]*4 for _ in range(N)] for _ in range(N)]
  # visited[y][x] 의 값은 4방향 각각에 대해 사용한 누적 거울 수를 의미한다.

  for i in range(4):
    visited[startY][startX][i] = 0
    queue.append((startY, startX, i))
  
  answer = float('inf')
  while queue:
    y, x, way = queue.popleft()

    if y == endY and x == endX:
      answer = min(answer, visited[y][x][way])
    
    nextY, nextX = findWay(y, x, way)
    
    if nextY < 0 or nextX < 0 or nextY >= N or nextX >= N: continue
    if GRAPH[nextY][nextX] in "*": continue

    # 길 존재
    if visited[nextY][nextX][way] == -1 or visited[nextY][nextX][way] > visited[y][x][way]:
      visited[nextY][nextX][way] = visited[y][x][way]
      queue.append((nextY, nextX, way))
    
    # 길 존재(거울을 놓을 수 있는 길)
    if GRAPH[nextY][nextX] in "!":
      if way < 2: # 이전에 동, 서 방향에서 왔다면 다음 방향은 남, 북
        for new_way in range(2, 4):
          if visited[nextY][nextX][new_way] == -1 or visited[nextY][nextX][new_way] > visited[y][x][way] + 1:
            visited[nextY][nextX][new_way] = visited[y][x][way] + 1
            queue.append((nextY, nextX, new_way))
      else: # 이전에 남, 북 방향에서 왔다면 다음 방향은 동, 서
        for new_way in range(2):
          if visited[nextY][nextX][new_way] == -1 or visited[nextY][nextX][new_way] > visited[y][x][way] + 1:
            visited[nextY][nextX][new_way] = visited[y][x][way] + 1
            queue.append((nextY, nextX, new_way))
  
  return answer

doors = []
for r in range(N):
  for c in range(N):
    if GRAPH[r][c] in '#':
      doors.append((r, c))

print(bfs(*doors[0], *doors[1]))