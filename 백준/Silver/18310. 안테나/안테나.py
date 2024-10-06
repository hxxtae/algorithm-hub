import sys
read = sys.stdin.readline

N = int(read().rstrip())
ARR = [*map(int, read().rstrip().split())]

ARR.sort()
print(ARR[(N-1) // 2])