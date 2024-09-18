import sys
read = sys.stdin.readline

N, M = map(int, read().rstrip().split())
ARR = [[*map(int, read().rstrip().split())] for _ in range(M)]

def underSix(cnt, arr):
  minPrice = float('inf')
  for priceA, priceB in arr:
    minPrice = min(minPrice, priceA, (priceB * cnt))
  return minPrice

def belowSix(arr):
  minPrice = float('inf')
  for priceA, priceB in arr:
    minPrice = min(minPrice, priceA, (priceB * 6))
  return minPrice

n = N
totalPrice = 0
while n > 0:
  if n >= 6:
    totalPrice += belowSix(ARR)
  else:
    totalPrice += underSix(n, ARR)
  n -= 6  

print(totalPrice)
