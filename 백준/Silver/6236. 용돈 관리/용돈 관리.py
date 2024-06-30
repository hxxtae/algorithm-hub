import sys
read = sys.stdin.readline

N, M = map(int, read().rstrip().split())
PAYLIST = [int(read().rstrip()) for _ in range(N)]

start = min(PAYLIST)
end = sum(PAYLIST)
maxPay = max(PAYLIST)
answer = 0

while start <= end:
  k = (start + end) // 2
  
  nowMoney = k
  m = 1
  for pay in PAYLIST:
    if nowMoney - pay < 0: # 인출을 하였는데 모자라게 되면
      nowMoney = k # 남은 금액은 통장에 집어넣고(없던 돈이라고하고) 다시 k 원을 인출한다.
      m += 1
    nowMoney -= pay
  
  if m > M or k < maxPay:
    start = k + 1
  elif m <= M:
    end = k - 1
    answer = k

print(answer)
