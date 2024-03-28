import sys
rl = sys.stdin.readline

N = int(rl().rstrip())
ARR = list(map(lambda _: rl().rstrip().split(' '), range(N)))

visitDict = dict()
for name, state in ARR:
  if state == 'enter':
    visitDict[name] = True
  elif state == 'leave':
    del visitDict[name]

print("\n".join(sorted(visitDict, reverse=True)))