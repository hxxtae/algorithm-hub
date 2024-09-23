import sys
read = sys.stdin.readline

BOARD = read().rstrip()

arr = []
cnt = 0
for c in BOARD:
  if c == 'X':
    cnt += 1
  else:
    if cnt > 0:
      if cnt % 2 != 0:
        cnt = -1
        break
      else:
        arr.append(('A' * 4 * (cnt // 4)) + ('B' * (cnt % 4)))
    cnt = 0
    arr.append('.')

if cnt == -1 or cnt == 1:
  print(-1)
else:
  if cnt % 2 != 0:
    print(-1)
  else:
    arr.append(('A' * 4 * (cnt // 4)) + ('B' * (cnt % 4)))
    print(''.join(arr))
    