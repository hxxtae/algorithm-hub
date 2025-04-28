def solution():
    N = int(input())
    A = sorted(map(int, input().split()))
    res = cnt = 0
    k = 2
    for i in range((N+1)//2):
        while k-1 < A[i]:
            cnt += 1
            k *= 2
        res += cnt
    print(res+1)

solution()