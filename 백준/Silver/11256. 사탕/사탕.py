import sys
read = sys.stdin.readline

t = int(read())
for _ in range(t) :
  j, n = map(int, read().split())

  data = []
  for _ in range(n) :
    a, b = map(int, read().split())
    data.append(a*b)

  data.sort(reverse=True)
  result = 0
  for i in range(len(data)) :
    j -= data[i]
    result += 1
    if j <= 0 :
      break

  print(result)