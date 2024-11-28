import sys
read = sys.stdin.readline

B, C, D = map(int, read().rstrip().split())
def readArr():
  return list(sorted(map(int, read().rstrip().split()), key=lambda x: -x))
arrB = readArr()
arrC = readArr()
arrD = readArr()

sum1 = sum(arrB) + sum(arrC) + sum(arrD)
sum2 = 0
for i in range(max(B, C, D)):
  if i < B and i < C and i < D:
    sum2 += (arrB[i] + arrC[i] + arrD[i]) * 0.9
  else:
    if i < B: sum2 += arrB[i]
    if i < C: sum2 += arrC[i]
    if i < D: sum2 += arrD[i]

print(sum1)
print(int(sum2))