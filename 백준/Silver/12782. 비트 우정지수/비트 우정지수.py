import sys
read = sys.stdin.readline

T = int(read())
 
for _ in range(T):
    n,m = map(str, read().split())
    one = 0
    zero = 0
    for i in range(len(n)):
        if n[i] != m[i]:
            if m[i] == '1':
                one += 1
            else:
                zero += 1
                
    print(max(one, zero))