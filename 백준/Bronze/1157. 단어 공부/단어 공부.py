import sys
rl = sys.stdin.readline

text = rl().rstrip()
textDict = dict()
maxChar = ''
maxCnt = 0

for c in text:
  c = c.upper()
  if c in textDict:
    textDict[c] += 1
  else:
    textDict[c] = 1

  if maxCnt == textDict[c]:
    maxChar = '?'
  if maxCnt < textDict[c]:
    maxCnt = textDict[c]
    maxChar = c

print(maxChar)