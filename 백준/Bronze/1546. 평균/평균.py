import sys
rl = sys.stdin.readline

N = int(rl().rstrip())
SCORES = list(map(int, rl().rstrip().split(' ')))

maxScore = max(SCORES)
answer = sum(map(lambda x: (x / maxScore) * 100, SCORES)) / N
print(answer)
