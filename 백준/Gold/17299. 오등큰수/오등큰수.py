import sys
read = sys.stdin.readline

N = int(read().rstrip())
ARR = [*map(int, read().rstrip().split())]

answer = [-1] * N
stack = [] # 값: [idx, num]
arrCnt = [0] * (max(ARR)+1)

# 값을 인덱스로 사용하여 각 숫자의 반복 개수 카운트
for num in ARR:
  arrCnt[num-1] += 1

for i, num in enumerate(ARR):
  while stack and arrCnt[stack[-1][1]-1] < arrCnt[num-1]:
    answer[stack[-1][0]] = num
    stack.pop()
  
  stack.append([i, num])

print(*answer)