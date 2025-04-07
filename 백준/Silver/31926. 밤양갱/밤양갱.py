import sys
input = sys.stdin.readline

N = int(input())
time = 8
daldidalgo = 1

while True:
    if daldidalgo > N:
        print(time+1)
        break
    elif daldidalgo == N:
        print(time+2)
        break
    else:
        daldidalgo *= 2
        time += 1