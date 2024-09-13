import sys
read = sys.stdin.readline

S = read().rstrip()

cntArr = [0, 0]
prev = ''
for i in S:
  if i == prev:
    continue
  
  cntArr[int(i)] += 1
  prev = i

print(min(cntArr))