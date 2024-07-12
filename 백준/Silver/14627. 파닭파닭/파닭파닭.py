import sys
input = sys.stdin.readline

s, c = map(int,input().split())
L = [int(input()) for _ in range(s)]

start = 0
end = 1000000000

resChick = 0

while(start<=end):
    mid = (start+end) // 2
    if mid == 0:
        mid = 1
        
    cnt = sum(pa//mid for pa in L)
    if cnt >= c:
        resChick = max(resChick,mid)
        start = mid+1
    else:
        end = mid -1
 
res = sum(L) - (c * resChick)
print(res)