import sys
read = sys.stdin.readline

n = int(read())
arr = list(map(int, read().split()))
arr.sort()

target = 1

for num in arr:
    if target < num:
        break

    target += num

print(target)