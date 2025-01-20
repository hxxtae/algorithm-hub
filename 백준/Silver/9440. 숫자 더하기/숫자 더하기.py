import sys
read = sys.stdin.readline

while True:
    num = list(map(int, read().split()))
    if num[0] == 0:
        break

    n = num[0]
    number = sorted(num[1:])
    
    num1, num2 = str(), str()
    for i in range(n):
        if number[i] != 0:
            num1, num2 = str(number[i]), str(number[i+1])
            number.pop(i)
            number.pop(i)
            break
    for i in range(0, len(number), 2 ):
        num1 += str(number[i])
        if i < len(number) - 1:
            num2 += str(number[i+1])


    print(int(num1) + int(num2))