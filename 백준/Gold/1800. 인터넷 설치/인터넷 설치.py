from heapq import *
import sys
read = sys.stdin.readline

N, P, K = map(int, read().rstrip().split())
GRAPH = [[*map(int, read().rstrip().split())] for _ in range(P)]

# 1. Set Graph
graph = [[] for _ in range(N+1)]
for a, b, dist in GRAPH:
  graph[a].append((dist, b))
  graph[b].append((dist, a))

def onDijkstra(base_cost):
  # 2. Set Distance
  distance = [float('inf')] * (N+1) # dist[n]: 1번부터 n번을 연결하는 데 사용된 공짜 케이블 개수 
  distance[1] = 0

  # 3. BFS
  heap = [(0, 1)]
  heapify(heap)
  while heap:
    dist, to = heappop(heap)
    
    if distance[to] < dist: continue

    for step_cost, step_to in graph[to]:
      free_dist = dist # dist: 공짜 케이블 선의 개수
      if step_cost > base_cost: # 기준 비용보다 큰 비용은 공짜 케이블로 대체하기 위해
        free_dist += 1 # 공짜 케이블 1개 추가
      
      if free_dist < distance[step_to]:
        distance[step_to] = free_dist
        heappush(heap, (free_dist, step_to))

  # 1번과 N번을 연결하는 데 K개 이하의 공짜 케이블이 사용된다면
  # base 가격은 정답이 될 수 있다.
  return distance[N]

if __name__ == '__main__':
  left = 0
  right = 1_000_000
  answer = -1

  while left <= right:
    mid = (left + right) // 2
    
    if onDijkstra(mid) <= K:
      answer = mid
      right = mid - 1
    else:
      left = mid + 1
  
  print(answer)