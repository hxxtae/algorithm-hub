while True:
    start, end = 1, 50
    N = int(input())
    
    if N == 0:
        break
    while True:
        n = (start + end) // 2
        print(n, end=' ')
        
        if n == N:
            break
        elif n > N:
            end = n - 1

        else:
            start = n + 1
    print(sep = '\n')