import sys
read = sys.stdin.readline

N = int(read().rstrip())
pays = [*map(int, read().rstrip().split())]
budget = int(read().rstrip())

start = 0
end = budget
answer = 0

while start <= end:
  mid = (start + end) // 2
  
  total = 0
  for pay in pays:
    if mid >= pay:
      total += pay
    else:
      total += mid
  
  if total <= budget:
    start = mid + 1
    answer = mid
  
  elif total > budget:
    end = mid - 1

if sum(pays) <= budget:
  print(max(pays))
else:
  print(answer)