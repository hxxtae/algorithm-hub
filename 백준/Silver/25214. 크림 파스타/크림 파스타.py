import sys
read = sys.stdin.readline

N = int(read().rstrip())
A = list(map(int,read().split()))

d = [0]*N
min_value = A[0]
for i in range(1,N):
    min_value = min(min_value,A[i])
    d[i] = max(d[i-1],A[i]-min_value)

print(*d)