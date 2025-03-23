import sys
input = sys.stdin.readline

t = int(input())
for tc in range(1, t + 1) :
  n = int(input())
  data = sorted(map(int, input().split()), reverse=True)
  result = []

  while data :
    price = data.pop()

    if price * 100//75 in data :
      result.append(str(price))
      data.remove(price * 100//75)

  print("Case #%d: %s" % (tc, " ".join(result)))