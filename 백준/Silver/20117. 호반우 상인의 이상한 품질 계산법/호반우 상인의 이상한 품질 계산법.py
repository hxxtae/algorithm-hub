n = int(input())
hos = list(map(int, input().split()))
hos.sort()

ans = sum(hos[(n+1)//2:]) * 2

if n % 2 == 1:
    ans += hos[n//2]

print(ans)