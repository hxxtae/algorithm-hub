import sys
read = sys.stdin.readline

N, K = map(int, read().rstrip().split())
numbers = [int(read().rstrip()) for _ in range(N)]

answer = 0
remain = K
for num in numbers[::-1]:
  if remain < num: continue
  
  answer += (remain // num)
  remain = (remain % num)

print(answer)