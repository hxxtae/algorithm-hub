import sys
read = sys.stdin.readline

n = int(read())
array = list(map(int, read().split()))
attack = array[0]
array = sorted(array[1:])
p = True
for i in array:
    if attack > i:
        attack += i
    else:
        p = False
        break
print('Yes' if p else 'No')