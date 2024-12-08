import sys
read = sys.stdin.readline

sound = input()

duck = ['q', 'u', 'a', 'c', 'k']
visited = [False] * len(sound)
total = 0
answer = 0

while total < len(sound):
    temp = []
    cnt = 0
    pos = 0

    for i in range(len(sound)):
        if visited[i]:
            continue

        if sound[i] != duck[pos]:
            continue
      
        visited[i] = True
        cnt += 1
        total += 1

        pos += 1
        if pos > 4:
            pos = 0
    
    if cnt % 5 != 0 or cnt == 0:
        answer = -1
        break

    answer += 1

print(answer)