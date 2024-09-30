import sys
read = sys.stdin.readline

N, M = list(map(int, read().rstrip().split()))
J = int(read().rstrip())
dropPos = [int(read().rstrip()) for _ in range(J)]

start = 1
end = M
answer = 0
for pos in dropPos:
  if start <= pos <= end:
    continue

  if start > pos:
    move = (start - pos)
    start -= move
    end -= move
    answer += move
  
  if end < pos:
    move = (pos - end)
    start += move
    end += move
    answer += move

print(answer)