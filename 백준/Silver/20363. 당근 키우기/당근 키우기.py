import math
import sys
read = sys.stdin.readline

X, Y = map(int, read().rstrip().split())

print(math.trunc(X + Y + (min(X, Y) / 10)))