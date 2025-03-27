import sys
input = sys.stdin.readline

m,s = map(int,input().split(':'))

count = 0
count += m // 10
count += m % 10

if s >= 30:
    count += 1
    count += (s-30) // 10
elif s < 30:
    count += 1
    count += s//10
print(count)