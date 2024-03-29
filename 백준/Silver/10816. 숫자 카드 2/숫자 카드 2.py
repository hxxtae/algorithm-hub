import sys
rl = sys.stdin.readline

N = int(rl().rstrip())
N_CARDS = rl().rstrip().split(' ')
M = int(rl().rstrip())
M_CARDS = rl().rstrip().split(' ')

cardDict = dict()
answer = []
for card in M_CARDS:
  cardDict[card] = 0

for card in N_CARDS:
  if card in cardDict:
    cardDict[card] += 1

for card in M_CARDS:
  answer.append(cardDict[card])

print(*answer)
