import sys
read = sys.stdin.readline

N = int(read().rstrip())
M = int(read().rstrip())
S = read().rstrip()

start = 0
length = 0
cnt = 0
while start < M - 1:
  if S[start:start+2+1] == 'IOI':
    start += 2
    length += 1
    if length == N:
      cnt += 1
      length -= 1
    continue

  start += 1
  length = 0

print(cnt)