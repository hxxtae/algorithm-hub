import sys
read = lambda: sys.stdin.readline().rstrip()
N = int(read())
books = [int(read()) for _ in range(N)]

find_target = N
answer = 0
for i in range(N-1, -1, -1):
    if books[i] != find_target:
        answer += 1
    else:
        find_target -= 1

print(answer)