import sys
read = sys.stdin.readline

def integer(x):
  return abs(int(x))

N = int(read().rstrip())
ARR1 = list(map(integer, read().rstrip().split()))
ARR2 = list(map(integer, read().rstrip().split()))

print(sum(ARR1) + sum(ARR2))