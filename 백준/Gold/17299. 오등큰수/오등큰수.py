import sys
read = sys.stdin.readline

N = int(read().rstrip())
ARR = [*map(int, read().rstrip().split())]

answer = [-1] * N
stack = [] # 값: [idx, num]
arrCnt = [0] * (max(ARR)+1)

# 값을 인덱스로 사용하여 각 숫자의 반복 개수 카운트
for num in ARR:
  arrCnt[num] += 1

# 오등큰수 찾아서 answer에 할당
for i in range(N):
  while stack and arrCnt[ARR[stack[-1]]] < arrCnt[ARR[i]]:
    answer[stack[-1]] = ARR[i]
    stack.pop()
  
  stack.append(i)

print(*answer)