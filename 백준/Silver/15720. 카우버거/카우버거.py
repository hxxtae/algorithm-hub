import sys
read = sys.stdin.readline

b, c, d = map(int, read().split())

burger = list(map(int, read().split()))
side = list(map(int, read().split()))
drink = list(map(int, read().split()))

burger.sort(reverse=True)
side.sort(reverse=True)
drink.sort(reverse=True)

result = 0
min_value = min(b, c, d)
for i in range(min_value) :
  result += (burger[i] + side[i] + drink[i]) * 0.9

result += sum(burger[min_value::])
result += sum(side[min_value::])
result += sum(drink[min_value::])

print(sum(burger) + sum(side) + sum(drink))
print(int(result))