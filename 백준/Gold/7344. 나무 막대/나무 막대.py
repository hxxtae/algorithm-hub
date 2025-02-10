import sys
from collections import deque
import heapq
import copy

read = sys.stdin.readline
sys.setrecursionlimit(100000000)

t=int(read())
for i in range(t):
    n=int(read())
    L1=list(map(int,read().split()))
    L2=[[L1[j],L1[j+1]] for j in range(0,n*2,2)]
    L2.sort()
    L2=deque(L2)
    L3=[[[0,0]]]
    for j in range(n):
        X=L2.popleft()
        flag=0
        for k in range(len(L3)):
            if X[0]>=L3[k][-1][0] and X[1]>=L3[k][-1][1]:
                L3[k].append(X)
                flag=1
                break
        if not flag:
            L3.append([X])
    print(len(L3))