import sys
read = sys.stdin.readline

N = int(read().rstrip())
A = [*map(int, read().rstrip().split())]
B = [*map(int, read().rstrip().split())]

A = sorted(A, key=lambda x: x)
B = sorted(B, key=lambda x: -x)

print(sum([A[i] * B[i] for i in range(N)]))