import sys
input = sys.stdin.readline

n, cnt1, cnt2 = int(input()), 0, 0
l = list(map(int, input().split()))
avg = sum(l) // n
for i in l:
    if i > avg+1: cnt1 += (i-avg-1)
    elif i < avg: cnt2 += (avg-i)
    
print(max(cnt1, cnt2))