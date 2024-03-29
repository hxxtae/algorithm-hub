import sys
rl = sys.stdin.readline

N = int(rl().rstrip())
chatSet = set()
totalCnt = 0
for _ in range(N):
  chat = rl().rstrip()
  if chat == 'ENTER':
    totalCnt += len(chatSet)
    chatSet.clear()
    continue

  chatSet.add(chat)

totalCnt += len(chatSet)
print(totalCnt)