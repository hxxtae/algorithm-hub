import sys
read = sys.stdin.readline

N, L = map(int, read().rstrip().split())
N_ARR = [*map(int, read().rstrip().split())]

l = L
nArr = sorted(N_ARR, key=lambda x: x)
for n in nArr:
  if l >= n:
    l += 1
  else:
    break

print(l)