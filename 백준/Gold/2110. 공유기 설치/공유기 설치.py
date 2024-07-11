import sys
read = sys.stdin.readline

N, C = map(int, read().rstrip().split())
X_ARR = [int(read().rstrip()) for _ in range(N)]

X_ARR.sort()

start = 1
end = X_ARR[-1] - X_ARR[0]
answer = 0

while start <= end:
  mid = (start + end) // 2
  current = X_ARR[0]
  count = 1
  
  # 공유기 설치 몇 대 할 수 있는지 체크
  for i in range(1, len(X_ARR)):
    if X_ARR[i] >= current + mid:      
      count += 1
      current = X_ARR[i] # 인접 시작위치 초기화

  # 공유기 설치 수가 목표 보다 크면 공유기 사이 거리 늘림
  if count >= C:
    start = mid + 1
    answer = mid
  # 공유기 설치 수가 목표 보다 작으면 공유기 사이 거리 줄임
  else:
    end = mid - 1

print(answer)