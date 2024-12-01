import sys
read = sys.stdin.readline
n = int(read())

length = list(map(int, read().split()))

total = 0
for i in range(n):
    total += length[i]

length.sort()

next = total
cost = 0
for i in range(n-1):
    next -= length[i]
    cost += (next*length[i])

print(cost)