import sys
read = sys.stdin.readline

S = read().rstrip()
T = read().rstrip()

answer = 0
arrS = list(S)
arrT = list(T)
while arrT:
  if arrT == arrS:
    answer = 1
    break

  if arrT[-1] == 'A':
    arrT.pop()
  else:
    arrT.pop()
    arrT.reverse()

print(answer)
