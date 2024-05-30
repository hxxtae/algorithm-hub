from heapq import *
from collections import deque
import sys
read = sys.stdin.readline

N, K = map(int, read().rstrip().split())
GRAPH = [[*map(int, read().rstrip().split())] for _ in range(K)]

def getParent(x, parent):
  if parent[x] != x:
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

def bfs(start):
  queue = deque([(0, start)]) # total, node
  visited = [0]*N
  visited[start] = 1
  total = 0

  while queue:
    expense, node = queue.popleft()

    total = max(total, expense)
    
    for next_expense, next in graph[node]:
      if visited[next]: continue
      visited[next] = 1
      queue.append((expense + next_expense, next))
  
  return total

parent = [i for i in range(N)]
heap = []
for a, b, expense in GRAPH:
  heap.append((expense, a, b))

heapify(heap)
answer = 0
cnt = 0
graph = [[] for _ in range(N)]

while heap:
  expense, a, b = heappop(heap)
  if not findParent(a, b, parent):
    unionParent(a, b, parent)
    answer += expense
    graph[a].append((expense, b))
    graph[b].append((expense, a))
    cnt += 1
    if cnt == (N-1): break

maxExpense = 0
for i in range(N):
  maxExpense = max(maxExpense, bfs(i))

print(answer)
print(maxExpense)
