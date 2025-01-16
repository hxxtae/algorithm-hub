import sys
read = sys.stdin.readline

n=int(read())
lst=[0]*(500001)
s=map(int,read().split())

for i in s:
    lst[i]+=1
print(max(lst))