import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
bear = [list(map(int, input().split())) for _ in range(k)]
bear.sort(reverse=True)

l = 0
r = 2**31

while l <= r:
    mid = (l+r) // 2

    sum_p = 0
    drink = 0
    for p, level in bear:   
        if mid >= level:
            sum_p += p
            drink += 1
        if drink == n:
            break

    if sum_p >= m and drink == n:
        r = mid - 1
    else:
        l = mid + 1

if r != 2**31:
    print(l)
else:
    print(-1)