import sys
rl = sys.stdin.readline

TEXT = rl().rstrip()

textSet = set()
textLen = len(TEXT)

for r in range(textLen):
  start = 0
  end = start + r
  while end < textLen:
    textSet.add(TEXT[start:end+1])
    start += 1
    end += 1

print(len(textSet))