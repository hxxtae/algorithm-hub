import sys
read = sys.stdin.readline

N, M = map(int, read().rstrip().split())
n_maps = [read().rstrip().split() for _ in range(N)]
m_list = [int(read().rstrip()) for _ in range(M)]

n_maps.sort(key=lambda x: int(x[1]))
answer = [''] * M

for i in range(M):
  start = 0
  end = N - 1
  num = m_list[i]

  while start <= end:
    mid = (start + end) // 2 # mid -> index

    name, power = n_maps[mid]
    if int(power) < num:
      start = mid + 1
    else:
      end = mid - 1
      answer[i] = name

print('\n'.join(answer))