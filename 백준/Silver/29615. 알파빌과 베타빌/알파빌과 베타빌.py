import sys
read = sys.stdin.readline

N, M = map(int, read().split())
citizenList = read().split()
friends = read().split()

result = 0
for c in citizenList[:M]:
    if c not in friends:
        result += 1

print(result)