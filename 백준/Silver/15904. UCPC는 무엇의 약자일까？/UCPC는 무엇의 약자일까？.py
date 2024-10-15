import sys
read = sys.stdin.readline

S = read().rstrip()

i = 0
for s in S:
  if i >= 4:
    break
  elif s == 'UCPC'[i]:
    i += 1

if i >= 4:
  print("I love UCPC")
else:
  print("I hate UCPC")