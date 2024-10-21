import sys
read = sys.stdin.readline

order = 1
while 1:
  S = read().rstrip()
  if '-' in S:
    break
  
  stack = []
  cnt = 0
  for s in S:
    if s == '{':
      stack.append(s)
    else:
      if stack:
        stack.pop()
      else:
        stack.append('{')
        cnt += 1
  
  cnt += (len(stack) // 2)
  print(f'{order}. {cnt}')
  order += 1