import sys
read = sys.stdin.readline

N = int(read().rstrip())
ARR = list(map(int, read().rstrip().split()))

link = []
for num in ARR:
  if not link or link[-1] < num:
    link.append(num)
  else:
    start = 0
    end = len(link) - 1
    
    while start <= end:
      mid = (start + end) // 2
      
      if link[mid] <= num:
        start = mid + 1
      else:
        end = mid - 1
    link[start] = num # 새로운 기준으로 업데이트
    # 반환 값으로 mid가 아닌 mid + 1 인 이유: 새롭게 업데이트 되는 경우는 같은 경우가 아닌 큰 경우이기 때문

print(len(link))