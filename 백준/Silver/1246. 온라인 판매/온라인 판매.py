import sys
read = sys.stdin.readline

N, M = map(int, read().rstrip().split())
pArr = [int(read().rstrip()) for _ in range(M)]

pArr.sort()
maxSale = 0
minA = 0
for i in range(M):
  p = pArr[i]
  sale = p * min(N, M - i)
  if maxSale < sale:
    maxSale = sale
    minA = p

print(minA, maxSale)
