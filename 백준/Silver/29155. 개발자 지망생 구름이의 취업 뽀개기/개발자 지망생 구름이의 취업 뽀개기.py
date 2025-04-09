import sys
input = sys.stdin.readline

N = int(input())
problems = list(map(int,input().split()))
times = [[] for _ in range(5)]
for _ in range(N):
    lev,time = map(int,input().split())
    times[lev-1].append(time)

for time in times:
    if time:
        time.sort()
res = -60

for i in range(5):
    first = False
    before_time = 0
    while problems[i] > 0:
        for j in range(len(times[i])):
            if not first:
                res+= times[i][j]
                before_time = times[i][j]
                first = True
            else:
                res += abs(before_time - times[i][j])
                res += times[i][j]
                before_time = times[i][j]
            problems[i]-=1
            if problems[i] == 0:
                res+=60
                break
print(res)