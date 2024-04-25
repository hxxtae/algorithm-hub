from collections import deque
import sys
read = sys.stdin.readline

N, M = map(int, read().rstrip().split())
S, E = map(int, read().rstrip().split())
GRAPH = [[*map(int, read().rstrip().split())] for _ in range(M)]

def getParent(x, parent):
  if x != parent[x]:
    parent[x] = getParent(parent[x], parent)
  return parent[x]

def unionParent(x, y, parent):
  a, b = [getParent(x, parent), getParent(y, parent)]
  if a > b: parent[a] = b
  else: parent[b] = a

def findParent(x, y, parent):
  a, b = [getParent(x, parent), getParent(y, parent)]
  if a == b: return True
  return False

def bfs(graph):
  queue = deque([[S, float('inf')]]) # (node, weight)
  visited = [0] * (N+1)
  visited[S] = 1
  answer = 0
  
  while queue:
    node, weight = queue.popleft()
    
    if node == E:
      answer = weight
      break
    
    for next, nextWeight in graph[node]:
      if visited[next]: continue
      visited[next] = 1
      queue.append([next, min(weight, nextWeight)])

  return answer

parent = [i for i in range(N+1)]
graph = sorted(GRAPH, key=lambda x: -x[2])
bfsGraph = [[] for _ in range(N+1)]

# 1. 최대 무게 내림차순으로 MST 구하기
for a, b, val in graph:
  if not findParent(a, b, parent):
    unionParent(a, b, parent)
    bfsGraph[a].append((b, val))
    bfsGraph[b].append((a, val))

# 2. BFS or DFS를 통해 MST를 탐색하여 S에서 시작하여 E까지 도달하였을 때의 최소 무게를 찾는다.
print(bfs(bfsGraph))