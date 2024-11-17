import sys
read = sys.stdin.readline

S = read().rstrip()
i = 0
n = 0
answer = 0
while True:
  n += 1
  for ss in str(n):
    if ss == S[i]:
      i += 1
      if i == len(S):
        print(n)
        exit()