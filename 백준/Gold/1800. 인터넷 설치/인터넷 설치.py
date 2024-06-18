import sys
import heapq
input = sys.stdin.readline
INF = float('INF')

def dijkstra(base):
    q = []
    heapq.heappush(q, (0, 1))
    dist = [INF for _ in range(N+1)]
    dist[1] = 0

    while q:
        d, now = heapq.heappop(q)

        if dist[now] < d:
            continue

        for (next, nextDist) in graph[now]:
            cost = d
            if nextDist > base:
                cost += 1

            if cost < dist[next]:
                dist[next] = cost
                heapq.heappush(q, (cost, next))

    return dist[N] <= K 


if __name__ == '__main__':
    
    N, P, K = map(int, input().split())
    graph = [[] for _ in range(N+1)]

    for _ in range(P):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))

    left = 0
    right = 1_000_000
    res = -1

    while left <= right:
        mid = (left + right) // 2

        if dijkstra(mid):
            res = mid
            right = mid - 1
        else:
            left = mid + 1

    print(res)