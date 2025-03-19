import sys
input = sys.stdin.readline

N = int(input())
A = sorted(map(int, input().split()))
sung_woo, park = 0, 0
for i in range(N):
    if i >= N//2:
        park += A[i]
    else:
        sung_woo += A[i]
print(sung_woo, park)