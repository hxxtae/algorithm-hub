import sys
read = sys.stdin.readline

X, Y = map(int, read().rstrip().split(' '))

z = (Y * 100) // X
scoreMin = 0
scoreMax = X

if z >= 99:
  print(-1)
else:
  while scoreMin <= scoreMax:
    mid = (scoreMin + scoreMax) // 2
    score = (((Y + mid) * 100) // (X + mid))

    if score <= z:
      scoreMin = mid + 1
  
    if score > z:
      scoreMax = mid - 1
  
  print(scoreMin)