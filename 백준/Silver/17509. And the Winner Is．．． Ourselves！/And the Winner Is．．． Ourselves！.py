import sys
read = sys.stdin.readline

lst = []
for i in range(11):
    lst.append(list(map(int,read().split(' '))))
lst.sort()
sum = 0
pen = 0
for i in range(11):
    pen += sum + lst[i][0]
    sum += lst[i][0]
    pen += 20*lst[i][1]
print(pen)