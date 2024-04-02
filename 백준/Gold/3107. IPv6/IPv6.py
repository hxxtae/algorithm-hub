import sys
read = sys.stdin.readline

IPV6 = read().rstrip()

answer = []
IPV6 = IPV6.split(':')
if IPV6[-1] == '':
  IPV6 = IPV6[:-1]
if IPV6[0] == '':
  IPV6 = IPV6[1:]

for s in IPV6:
  if s == '':
    answer.append('')
    continue
  answer.append(s.zfill(4))

while len(answer) < 8:
  answer.insert(answer.index(''), '0000')

if '' in answer:
  answer.insert(answer.index(''), '0000')
  answer.remove('')

print(":".join(answer))