import sys
read = sys.stdin.readline

Y, X = map(int, read().rstrip().split())
ARR = [list([*read().rstrip()]) for _ in range(Y)]

count = 0

def flipCoin(y, x):
  for i in range(y, -1, -1):
    for j in range(x, -1, -1):
      coin = ARR[i][j]
      if coin == '1': ARR[i][j] = '0'
      else: ARR[i][j] = '1'

for i in range(Y-1, -1, -1):
  for j in range(X-1, -1, -1):
    if ARR[i][j] == '0': continue    
    flipCoin(i, j)
    count += 1

print(count)