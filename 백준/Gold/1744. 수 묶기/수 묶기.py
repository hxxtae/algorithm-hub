import sys
read = sys.stdin.readline

N = int(read().rstrip())
ARR = [int(read().rstrip()) for _ in range(N)]

# 양수 부분
plusARR = list(sorted(filter(lambda x: x > 0, ARR), key=lambda x: -x))

# 음수 부분
minusARR = list(sorted(filter(lambda x: x <= 0, ARR), key=lambda x: -abs(x)))

plus = 0
minus = 0

if len(plusARR) % 2: plus += plusARR.pop()
for i in range(0, len(plusARR), 2):
  a = (plusARR[i] * plusARR[i+1])
  b = plusARR[i] + plusARR[i+1]
  if a > b: plus += a
  else: plus += b
  

if len(minusARR) % 2: minus += minusARR.pop()
for i in range(0, len(minusARR), 2):
  minus += (minusARR[i] * minusARR[i+1])

print(max(sum(ARR), (plus + minus)))
