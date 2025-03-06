import sys
from heapq import *
read = sys.stdin.readline

n, m = map(int, read().split())
n *= 24 #n일이므로 24를 곱해서 시간으로 맞춰준다.
base_score = list(map(int, read().split())) #기존 점수 list
tmp = list(map(int, read().split()))
plus_score = []
for i in range(m):
    plus_score.append([-tmp[i], i]) #[시간 당 추가 점수, index]의 원소로 구성된 추가 점수 list. 최대힙으로 사용할 것이기에 0번째 원소에 마이너스 취해준다.
heapify(plus_score) #우선순위 큐로 바꾸기
while plus_score: #큐가 빌 때까지
    plus, idx = heappop(plus_score)
    plus *= -1 #마이너스 붙은채로 저장되어 있으므로 다시 변환
    x = (100 - base_score[idx]) // plus #plus를 통해 손실 없이 채울 수 있는 수. ex. base_score = 60, plus = 3이라면, 총 39점을 손실 없이 채울 수 있고 x = 13이 된다.
    if (100 - base_score[idx]) % plus: #남는 점수가 있다면
        heappush(plus_score, [-(100 - base_score[idx] - x * plus), idx]) #남는 만큼 우선순위 큐에 삽입
    if x >= n: #남는 시간보다 x가 크다면 (>= 아니라 > 여도 상관 없음)
        x = n #남는 시간만큼 모두 쓰기
    base_score[idx] += plus * x #점수 더해주고
    n -= x #공부 시간만큼 차감
    if n == 0: #모든 시간 공부를 마쳤다면
        break #끝
print(sum(base_score)) #점수의 합 출력