import sys
read = sys.stdin.readline

N = int(read().rstrip())
STR = read().rstrip()

red = 0
blue = 0
curr = ''
for s in STR:
  if s != curr:
    curr = s
    if curr == 'B': blue += 1
    elif curr == 'R': red += 1

print(min(red, blue) + 1)
