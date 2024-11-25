import sys
read = sys.stdin.readline

n = int(read())
a, b = map(int, read().split())
c = int(read())
topping = [int(read()) for _ in range(n)]
topping.sort(reverse=True)
result = c // a
d = c
price = a
for k in range(n):
    price += b
    d += topping[k]
    result = max(result, d // price)
print(result)