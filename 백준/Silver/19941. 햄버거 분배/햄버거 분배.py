import sys
read = sys.stdin.readline

N, K = map(int, read().rstrip().split())
table = [*read().rstrip()]

answer = 0
for i in range(N):
  if table[i] == "P":
    for j in range(max(0, i - K), min(i + K + 1, N)):
      if table[j] == "H":
        table[j] = "D"
        answer += 1
        break

print(answer)