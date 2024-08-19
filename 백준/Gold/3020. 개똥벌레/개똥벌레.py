import sys
read = sys.stdin.readline

N, H = map(int, input().split())

lines = [0] * H
for i in range(N):
  size = int(input())
  if i % 2 == 0:
    lines[H-size] += 1
  else:
    lines[0] += 1
    lines[size] -= 1

for i in range(1, H):
  lines[i] += lines[i-1]

result = 0
low = min(lines)
for l in lines:
  if l == low:
    result += 1
        
print(low, result)