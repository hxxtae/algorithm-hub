import sys
N, A, D = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))

cnt = 0
x = 0
for i in range(N):
    if arr[i] == A + (x*D):
        cnt += 1
        x += 1
print(cnt)