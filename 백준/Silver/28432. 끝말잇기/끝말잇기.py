import sys
read = sys.stdin.readline

N = int(read().rstrip())
TEXTS = [read().rstrip() for _ in range(N)]
M = int(read().rstrip())
ANSWERS = [read().rstrip() for _ in range(M)]

qMarkIdx = 0
textDict = set()
TEXTS.append('-')
TEXTS.insert(0, '-')
for i, text in enumerate(TEXTS):
  textDict.add(text)
  if text == "?":
    qMarkIdx = i

prevTextChr = TEXTS[qMarkIdx - 1][-1] # 이전 글자 맨 뒤 단어
nextTextChr = TEXTS[qMarkIdx + 1][0] # 다음 글자 맨 앞 단어

answerArr = []
for text in ANSWERS:
  if prevTextChr == "-" and nextTextChr == "-":
    answerArr.append(text)

  if prevTextChr == "-" and text[-1] == nextTextChr:
    answerArr.append(text)

  if nextTextChr == "-" and text[0] == prevTextChr:
    answerArr.append(text)

  if text[0] == prevTextChr and text[-1] == nextTextChr:
    answerArr.append(text)

answer = list(filter(lambda x: x not in textDict, answerArr))
print(answer[0])
