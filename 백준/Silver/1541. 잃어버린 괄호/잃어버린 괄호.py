import sys
read = sys.stdin.readline

ARR = [*read().rstrip()]

confirm = False
strNum = ''
answer = 0
for item in ARR:
  if item.isdecimal():
    strNum += item
  else:
    if confirm:
      answer -= int(strNum)
    else:
      answer += int(strNum)
    
    if item == '-':
      confirm = True
    strNum = ''

if confirm:
  answer -= int(strNum)
else:
  answer += int(strNum)

print(answer)