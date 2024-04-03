import sys
from collections import deque
read = sys.stdin.readline

N = int(read().rstrip())
ARR = [*map(int, read().rstrip().split(' '))]

balloon = [*map(lambda x: [x[0]+1, x[1]], enumerate(ARR))]
deq = deque(balloon)

answer = []
while deq:
  order, move = deq.popleft()
  answer.append(order)

  if move > 0:
    # move가 양수인 경우, 위에서 이미 poleft를 수행하였기 때문에 -> 이미 왼쪽으로 한칸 회전 -> move-1
    # roate(n): n값이 음수이면 deq를 왼쪽으로 회전
    deq.rotate(-(move-1))
  if move < 0:
    # move가 음수인 경우
    # roate(n): n값이 양수이면 deq를 오른쪽으로 회전
    deq.rotate(-(move))
  
print(*answer)