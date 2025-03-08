import sys
read = sys.stdin.readline

A = read().strip()
B = read().strip()
start = 0
count = 0

while start < len(A):
  if B == A[start:start + len(B)]:
    count += 1
    start += len(B)
  else:
    start += 1

print(count)