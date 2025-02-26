import sys
read = sys.stdin.readline

k = int(read())

size = 1

count = 0
while size < k:
    size = size << 1
    
result1 = size

while k > 0:
    if k >= size:
        k -= size
    else:
        size //= 2
        count += 1

print(result1, count)