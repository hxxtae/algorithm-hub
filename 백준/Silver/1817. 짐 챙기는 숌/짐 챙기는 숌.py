import sys
read = sys.stdin.readline

N, M = [*map(int, read().rstrip().split())]
ARR = [*map(int, read().rstrip().split())]

cnt = 1
bookSum = 0
for book in ARR:
  if (bookSum + book) > M:
    cnt += 1
    bookSum = book
  else:
    bookSum += book

if N == 0: print(0)
else: print(cnt)