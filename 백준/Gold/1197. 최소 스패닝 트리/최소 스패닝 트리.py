import sys
read = sys.stdin.readline

V, E = [*map(int, read().rstrip().split())]
GRAPH = [[*map(int, read().rstrip().split())] for _ in range(E)]

# NOTE_1: 가중치 오름차순 정렬
graph = sorted(GRAPH, key=lambda x: x[2])
# NOTE_2: 집합 선언
parent = [i for i in range(V+1)]

# NOTE_3: union-find 알고리즘
def getParent(x, parent):
  return x if parent[x] == x else getParent(parent[x], parent)

def unionParent(x, y, parent):
  a, b = [getParent(x, parent), getParent(y, parent)]
  if a > b: parent[a] = b
  else: parent[b] = a

def findParent(x, y, parent):
  a, b = [getParent(x, parent), getParent(y, parent)]
  if a == b: return True
  else: return False

answer = 0
for a, b, val in graph:
  # 💡 사이클 방지 -> 이미 연결된 노드는 PASS
  if not findParent(a, b, parent):
    # 💡 노드 연결(집합에 노드 추가)
    unionParent(a, b, parent)
    answer += val

print(answer)
