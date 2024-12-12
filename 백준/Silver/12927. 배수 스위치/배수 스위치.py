import sys
read = sys.stdin.readline

ARR = [*read().rstrip()]

answer = 0
for i in range(0, len(ARR)):
  if ARR[i] == "N": continue
  else: ARR[i] = "N"

  for j in range(i+1, len(ARR)):
    if ARR[j] == "Y":
      if (j + 1) % (i + 1) == 0: ARR[j] = "N"
    else:
      if (j + 1) % (i + 1) == 0: ARR[j] = "Y"

  answer += 1

if "Y" in ARR:
  print(-1)
else:
  print(answer)
