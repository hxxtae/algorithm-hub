import sys
input = sys.stdin.readline


def binary_search(v, dir):
    left, right = 0, n-1

    while left <= right:
        mid = (left+right)//2

        if v < a[mid]:
            right = mid-1
        elif v > a[mid]:
            left = mid+1
        else:
            return mid

    if dir == 0:
        return left
    else:
        return right


n, m = map(int, input().split())
a = sorted(list(map(int, input().split())))

for _ in range(m):
    s, e = map(int, input().split())
    l, r = binary_search(s, 0), binary_search(e, 1)
    print(r-l+1)