import sys
read = sys.stdin.readline

N = int(read().rstrip())
roads = [*map(int, read().rstrip().split())]
prices = [*map(int, read().rstrip().split())]

answer = prices[0] * roads[0]
prevPrice = prices[0]
for i in range(1, N-1):
  price, road = [prices[i], roads[i]]
  
  # 다음 주유소 가격이 더 저렴하다면
  if prevPrice > price:
    answer += (price * road)
    prevPrice = price
  # 지금까지 방문한 주유소 가격이 가장 저렴하다면
  else:
    answer += (prevPrice * road)

print(answer)
