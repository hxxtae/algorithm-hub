import sys
read = sys.stdin.readline

def flip(x, y): #동전을 뒤집는 함수 

    for i in range(x + 1):

        for j in range(y + 1):

            if coin[i][j]==1:

                coin[i][j]=0
            
            else:
                coin[i][j]=1


N, M = map(int, read().split())

coin = [list(map(int, list(read().strip()))) for _ in range(N)]

cnt = 0

for i in range(N - 1, -1, -1):

    for j in range(M - 1, -1, -1): #가장 오른쪽 아래부터 거꾸로 내려온다.

        if coin[i][j]:

            cnt += 1

            flip(i, j)

print(cnt)