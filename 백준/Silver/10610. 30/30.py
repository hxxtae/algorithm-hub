import sys
read = sys.stdin.readline

N = list(read().rstrip())
N.sort(reverse=True)

sumNum = sum(map(int, N))

if (sumNum % 3) != 0 or '0' not in N:
  print(-1)
else:
  print(''.join(N))