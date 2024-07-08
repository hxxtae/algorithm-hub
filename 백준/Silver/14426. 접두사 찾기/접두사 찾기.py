import sys
read = sys.stdin.readline

N, M = map(int, read().rstrip().split())
N_ARR = [read().rstrip() for _ in range(N)]
M_ARR = [read().rstrip() for _ in range(M)]

N_ARR.sort()
M_ARR.sort()

cnt = 0
i = 0
j = 0
while i < N and j < M:
  if M_ARR[j] == N_ARR[i][:len(M_ARR[j])]:
    cnt += 1
    j += 1
    continue

  if N_ARR[i] > M_ARR[j]: # S에 포함된 문자열이 사전 순으로 더 뒤에있는 경우
    j += 1
    continue
  
  if M_ARR[j] > N_ARR[i]: # S에 포함된 문자열이 사전 순으로 더 앞에있는 경우
    i += 1
    continue

print(cnt)